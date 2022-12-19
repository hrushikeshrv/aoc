from time import time

with open("inputs/input-19.txt", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

lines = [
    "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
    "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.",
]


def get_blueprint_costs(blueprint):
    costs = {}
    l = blueprint.split()
    costs["ore"] = (int(l[6]), 0, 0)  # (ore cost, clay cost, obsidian cost)
    costs["clay"] = (int(l[12]), 0, 0)
    costs["obsidian"] = (int(l[18]), int(l[21]), 0)
    costs["geode"] = (int(l[27]), 0, int(l[30]))
    return costs


def get_max_geodes(
    costs,
    n_ore=0,
    n_clay=0,
    n_obsidian=0,
    n_geodes=0,
    n_ore_robots=1,
    n_clay_robots=0,
    n_obsidian_robots=0,
    n_geode_robots=0,
    minutes_left=24,
    cache={}
):
    if minutes_left <= 1:
        return n_geodes
    # if (n_ore, n_clay, n_obsidian, n_geodes, minutes_left) in cache:
    #     return n_geodes + cache[(n_ore, n_clay, n_obsidian, n_geodes, minutes_left)]

    results = [
        get_max_geodes(
            costs,
            n_ore + n_ore_robots,
            n_clay + n_clay_robots,
            n_obsidian + n_obsidian_robots,
            n_geodes + n_geode_robots,
            n_ore_robots,
            n_clay_robots,
            n_obsidian_robots,
            n_geode_robots,
            minutes_left - 1,
            cache
        )
    ]

    if n_ore >= costs["ore"][0]:
        # We can build an ore robot
        results.append(
            get_max_geodes(
                costs,
                n_ore - costs['ore'][0] + n_ore_robots,
                n_clay + n_clay_robots,
                n_obsidian + n_obsidian_robots,
                n_geodes + n_geode_robots,
                n_ore_robots + 1,
                n_clay_robots,
                n_obsidian_robots,
                n_geode_robots,
                minutes_left - 1,
                cache
            )
        )

    if n_ore >= costs["clay"][0]:
        # We can build a clay robot
        results.append(
            get_max_geodes(
                costs,
                n_ore - costs['clay'][0] + n_ore_robots,
                n_clay + n_clay_robots,
                n_obsidian + n_obsidian_robots,
                n_geodes + n_geode_robots,
                n_ore_robots,
                n_clay_robots + 1,
                n_obsidian_robots,
                n_geode_robots,
                minutes_left - 1,
                cache
            )
        )

    if n_ore >= costs["obsidian"][0] and n_clay >= costs["obsidian"][1]:
        # We can build an obsidian robot
        results.append(
            get_max_geodes(
                costs,
                n_ore - costs['obsidian'][0] + n_ore_robots,
                n_clay - costs['obsidian'][1] + n_clay_robots,
                n_obsidian + n_obsidian_robots,
                n_geodes + n_geode_robots,
                n_ore_robots,
                n_clay_robots,
                n_obsidian_robots + 1,
                n_geode_robots,
                minutes_left - 1,
                cache
            )
        )

    if n_ore >= costs["geode"][0] and n_obsidian >= costs["geode"][2]:
        # We can build a geode robot
        results.append(
            get_max_geodes(
                costs,
                n_ore - costs['geode'][0] + n_ore_robots,
                n_clay + n_clay_robots,
                n_obsidian - costs['geode'][2] + n_obsidian_robots,
                n_geodes + n_geode_robots,
                n_ore_robots,
                n_clay_robots,
                n_obsidian_robots,
                n_geode_robots + 1,
                minutes_left - 1,
                cache
            )
        )
    
    ans = max(results)
    # cache[(n_ore, n_clay, n_obsidian, n_geodes, minutes_left)] = ans
    return ans

tic = time()
print(get_max_geodes(get_blueprint_costs(lines[0]), minutes_left=25))
toc = time()
print(f'Took {toc-tic}s')

def solve1(blueprints):
    score = 0
    for i, bluep in enumerate(blueprints):
        score += (i + 1) * get_max_geodes(get_blueprint_costs(bluep), minutes_left=25)
    return score

# print(solve1(lines))
