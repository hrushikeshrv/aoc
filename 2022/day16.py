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


def floyd_warshall(valve_graph):
    distances = {u: {v: 1e10 for v in valve_graph} for u in valve_graph}
    for i in valve_graph:
        distances[i][i] = 0
        for n in valve_graph[i][1]:
            distances[i][n] = 1

    for i in valve_graph:
        for j in valve_graph:
            for k in valve_graph:
                distances[j][k] = min(
                    distances[j][k], distances[j][i] + distances[i][k]
                )

    return distances


distances = floyd_warshall(valves)


def get_score(valve_graph, traversal):
    score = 0
    for node in traversal:
        score += valve_graph[node][0] * traversal[node]
    return score


def get_traversals(distances, valve_graph, time=30, cur="AA", chosen={}):
    yield chosen

    for nxt in valve_graph[cur][1]:
        if valve_graph[nxt][0] == 0:
            continue
        new_time = time - (distances[cur][nxt] + 1)
        if new_time < 2:
            return
        new_chosen = chosen | {nxt: new_time}
        new_valves = valve_graph.copy()
        # del new_valves[nxt]
        yield from get_traversals(distances, new_valves, new_time, nxt, new_chosen)


best = max(get_score(valves, c) for c in get_traversals(distances, valves))
print(best)
