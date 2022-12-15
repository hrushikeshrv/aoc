with open("inputs/input-15.txt", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

coords = []
for line in lines:
    l = (
        line.replace("Sensor at ", "")
        .replace(": closest beacon is at ", " ")
        .replace(",", "")
        .replace("x=", "")
        .replace("y=", "")
        .split()
    )
    coords.append((int(l[0]), int(l[1]), int(l[2]), int(l[3])))


def solve1(sensor_grid, row):
    no_beacon_set = set()
    for s in sensor_grid:
        sensor_x = s[0]
        sensor_y = s[1]
        distance = abs(s[0] - s[2]) + abs(s[1] - s[3])
        remaining_distance = distance - abs(row - sensor_y)
        if remaining_distance < 0:
            continue
        if (sensor_x, row) != (s[2], s[3]):
            no_beacon_set.add(sensor_x)
        for i in range(1, remaining_distance + 1):
            if (sensor_x - i, row) != (s[2], s[3]):
                no_beacon_set.add(sensor_x - i)
        for i in range(1, remaining_distance + 1):
            if (sensor_x + i, row) != (s[2], s[3]):
                no_beacon_set.add(sensor_x + i)
    return len(no_beacon_set)


print(solve1(coords, 2000000))
# Answer was 4665948


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged_ranges = []
    for i in range(len(ranges) - 1):
        r1 = ranges[i]
        r2 = ranges[i + 1]
        if r2[0] <= r1[1] <= r2[1] or r2[0] == r1[1] + 1:
            ranges[i + 1] = [r1[0], r2[1]]
        elif r1[0] <= r2[0] and r1[1] >= r2[1]:
            ranges[i + 1] = r1
            continue
        else:
            merged_ranges.append(r1)
    merged_ranges.append(ranges[-1])
    return merged_ranges


def solve2(sensor_grid):
    for row in range(4000001):
        no_beacon_list = []
        for s in sensor_grid:
            sensor_x = s[0]
            sensor_y = s[1]
            distance = abs(s[0] - s[2]) + abs(s[1] - s[3])
            remaining_distance = distance - abs(row - sensor_y)
            if remaining_distance < 0:
                continue
            no_beacon_list.append(
                [sensor_x - remaining_distance, sensor_x + remaining_distance]
            )
        no_beacon_ranges = merge_ranges(no_beacon_list)
        if len(no_beacon_ranges) > 1:
            return 4000000 * (no_beacon_ranges[0][1] + 1) + row


print(solve2(coords))
# Answer was 13543690671045
