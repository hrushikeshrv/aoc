with open("inputs/input-05.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_loc(seed, maps):
    obj = seed
    for obj_map in maps:
        for obj_start, obj_end, dest_start, dest_end in obj_map:
            if obj_start <= obj <= obj_end:
                obj = dest_start + obj - obj_start
                break
    return obj


def get_maps(lines):
    maps = []
    curr_map = []
    for line in lines[1:]:
        if line.strip() == "":
            continue
        if line[0].isalpha():
            if curr_map:
                maps.append(curr_map)
            curr_map = []
            continue
        line = line.split()
        curr_map.append(
            (
                int(line[1]),
                int(line[1]) + int(line[2]) - 1,
                int(line[0]),
                int(line[0]) + int(line[2]) - 1,
            )
        )
    maps.append(curr_map)
    return maps


def solve1(lines):
    seeds = lines[0].split(":")[1].split()
    maps = get_maps(lines)
    min_loc = None
    for seed in seeds:
        _ = get_loc(int(seed), maps)
        if not min_loc:
            min_loc = _
        min_loc = min(min_loc, _)
    return min_loc


# Very inefficient solution that starts from the bottom, but it works :)
def solve2(lines):
    seeds = lines[0].split(":")[1].split()
    maps = get_maps(lines)

    for obj_map in maps:
        for i in range(len(obj_map)):
            obj_map[i] = (obj_map[i][2], obj_map[i][3], obj_map[i][0], obj_map[i][1])

    maps = list(reversed(maps))
    i = 0
    while True:
        i += 1
        _ = get_loc(i, maps)
        for j in range(0, len(seeds), 2):
            if int(seeds[j]) <= _ < int(seeds[j]) + int(seeds[j + 1]):
                return i


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
