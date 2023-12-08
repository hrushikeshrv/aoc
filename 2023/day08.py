from math import gcd

with open("inputs/input-08.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        _ = line.split("(")[1].split(",")
        nodes[line[:3]] = (_[0], _[1].strip()[:-1])

    node = "AAA"
    i = 0
    while True:
        if directions[i % len(directions)] == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        i += 1
        if node == "ZZZ":
            return i


def solve2(lines):
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        _ = line.split("(")[1].split(",")
        nodes[line[:3]] = (_[0], _[1].strip()[:-1])

    curr_nodes = [node for node in nodes if node.endswith("A")]
    finish_times = []
    for idx in range(len(curr_nodes)):
        curr_node = curr_nodes[idx]
        i = 0
        while True:
            if directions[i % len(directions)] == "L":
                curr_node = nodes[curr_node][0]
            else:
                curr_node = nodes[curr_node][1]
            i += 1
            if curr_node.endswith("Z"):
                finish_times.append(i)
                break
    steps = 1
    for i in finish_times:
        steps = steps * i // gcd(steps, i)
    return steps


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
