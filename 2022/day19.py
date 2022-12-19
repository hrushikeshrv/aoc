from collections import deque

with open("inputs/input-19.txt", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_blueprint_costs(blueprint):
    costs = {}
    l = blueprint.split()
    costs["ore"] = (int(l[6]), 0, 0)  # (ore cost, clay cost, obsidian cost)
    costs["clay"] = (int(l[12]), 0, 0)
    costs["obsidian"] = (int(l[18]), int(l[21]), 0)
    costs["geode"] = (int(l[27]), 0, int(l[30]))
    return costs


def get_max_geodes(costs, time_left):
    best = 0
    state = (0, 0, 0, 0, 1, 0, 0, 0, time_left)
    max_ore = max(costs[x][0] for x in costs)
    max_clay = costs['obsidian'][1]
    max_obs = costs['geode'][2]
    q = deque()
    q.append(state)
    seen = set()
    while q:
        s = q.popleft()
        n_ore, n_clay, n_obs, n_geo, n_ore_r, n_clay_r, n_obs_r, n_geo_r, t = s
        if best > n_geo + t * n_geo_r + t * (t - 1) / 2:
            continue
        best = max(best, n_geo)
        if t == 0:
            continue
            
        if s in seen:
            continue
        seen.add(s)
        
        if n_ore >= costs['geode'][0] and n_obs >= costs['geode'][2]:
            q.append((n_ore - costs['geode'][0] + n_ore_r, n_clay + n_clay_r, n_obs - costs['geode'][2] + n_obs_r, n_geo + n_geo_r,
                      n_ore_r, n_clay_r, n_obs_r, n_geo_r + 1, t - 1))
        else:
            q.append((n_ore + n_ore_r, n_clay + n_clay_r, n_obs + n_obs_r, n_geo + n_geo_r, n_ore_r, n_clay_r, n_obs_r,
                      n_geo_r, t - 1))
            if n_ore >= costs['ore'][0] and n_ore_r <= max_ore and n_ore < max_ore * t:
                q.append((n_ore - costs['ore'][0] + n_ore_r, n_clay + n_clay_r, n_obs + n_obs_r, n_geo + n_geo_r, n_ore_r + 1, n_clay_r, n_obs_r, n_geo_r, t-1))
            if n_ore >= costs['clay'][0] and n_clay_r <= max_clay and n_clay < max_clay * t:
                q.append((n_ore - costs['clay'][0] + n_ore_r, n_clay + n_clay_r, n_obs + n_obs_r, n_geo + n_geo_r,
                          n_ore_r, n_clay_r + 1, n_obs_r, n_geo_r, t - 1))
            if n_ore >= costs['obsidian'][0] and n_clay >= costs['obsidian'][1] and n_obs_r <= max_obs and n_obs < max_obs * t:
                q.append((n_ore - costs['obsidian'][0] + n_ore_r, n_clay - costs['obsidian'][1] + n_clay_r, n_obs + n_obs_r, n_geo + n_geo_r,
                          n_ore_r, n_clay_r, n_obs_r + 1, n_geo_r, t - 1))
    
    return best


def solve1(blueprints):
    score = 0
    for i, bluep in enumerate(blueprints):
        score += (i + 1) * get_max_geodes(get_blueprint_costs(bluep), 24)
    return score

print(solve1(lines))


def solve2(blueprints):
    score = 1
    for b in blueprints:
        score *= get_max_geodes(get_blueprint_costs(b), 32)
    return score


print(solve2(lines[:3]))
