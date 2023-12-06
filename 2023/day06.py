with open("inputs/input-06.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_distance(time_held, total_time):
    return (total_time - time_held) * time_held


def solve1(lines):
    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()
    ans = 1

    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        start_time = 1
        end_time = time
        for held_time in range(time):
            if get_distance(held_time, time) > distance:
                start_time = held_time
                break
        for held_time in range(time, 0, -1):
            if get_distance(held_time, time) > distance:
                end_time = held_time
                break
        ans *= end_time - start_time + 1
    return ans


def solve2(lines):
    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))
    start_time = 1
    end_time = time
    for held_time in range(time):
        if get_distance(held_time, time) > distance:
            start_time = held_time
            break
    for held_time in range(time, 0, -1):
        if get_distance(held_time, time) > distance:
            end_time = held_time
            break
    return end_time - start_time + 1


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
