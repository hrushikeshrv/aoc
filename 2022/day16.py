with open("inputs/input-16.txt", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

lines = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]

valves = {}
for line in lines:
    l = (
        line.replace("tunnel leads to valve", "tunnels lead to valves")
        .replace("Valve ", "")
        .replace(" has flow rate=", " ")
        .replace("; tunnels lead to valves", "")
        .replace(",", "")
        .split()
    )
    valves[l[0]] = (int(l[1]), l[2:])


def max_flow(valve_graph, path, minutes_left):
    if minutes_left < 1:
        return 0
    current_node = path[-1]

    candidates = []
    for neighbour in valve_graph[current_node][1]:
        if neighbour not in path:
            path.append(neighbour)
            candidates.append(
                valve_graph[current_node][0] * (minutes_left - 1)
                + max_flow(valve_graph, path, minutes_left - 2)
            )
            candidates.append(max_flow(valve_graph, path, minutes_left - 1))
            path.pop()
    if not candidates:
        return 0
    return max(candidates)


print(max_flow(valves, ["AA"], 30))
