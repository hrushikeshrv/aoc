with open('inputs/input-15.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

# lines = [
#     'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
#     'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
#     'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
#     'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
#     'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
#     'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
#     'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
#     'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
#     'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
#     'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
#     'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
#     'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
#     'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
#     'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
# ]

coords = []
for line in lines:
    l = line.replace('Sensor at ', '').replace(': closest beacon is at ', ' ').replace(',', '').replace('x=', '').replace('y=', '').split()
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


