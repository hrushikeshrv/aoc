with open('inputs/input-09.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_guid(idx):
    return idx // 2


def solve1(lines):
    lines = [int(x) for x in lines[0]]
    left_idx = 0
    left_pos = 0
    right_idx = len(lines) - 1

    checksum = 0
    while left_idx <= right_idx:
        # Left pointer points to data
        if left_idx % 2 == 0:
            for i in range(lines[left_idx]):
                checksum += get_guid(left_idx) * left_pos
                left_pos += 1
            left_idx += 1
        # Left pointer points to empty space
        else:
            for i in range(lines[left_idx]):
                checksum += get_guid(right_idx) * left_pos
                left_pos += 1
                if i + 1 >= int(lines[right_idx]):
                    lines[left_idx] = lines[left_idx] - lines[right_idx]
                    right_idx -= 2
                    break
            else:
                lines[right_idx] = lines[right_idx] - lines[left_idx]
                left_idx += 1
    return checksum


def solve2(lines):
    line = [int(x) for x in lines[0]]
    occupied = {}
    free = []
    left_pos = 0
    space_flag = False
    guid = 0
    for i in line:
        if not space_flag:
            occupied[guid] = [left_pos, left_pos + i - 1]
            left_pos += i
            guid += 1
            space_flag = True
        else:
            free.append([left_pos, left_pos + i - 1])
            left_pos += i
            space_flag = False

    relocated_keys = set()
    gap_found = True
    while gap_found:
        gap_found = False
        for key in reversed(occupied.keys()):
            if key in relocated_keys:
                continue
            occupied_len = occupied[key][1] - occupied[key][0] + 1
            for i, free_range in enumerate(free):
                free_len = free_range[1] - free_range[0] + 1
                if free_len >= occupied_len and free_range[0] < occupied[key][0]:
                    gap_found = True
                    relocated_keys.add(key)
                    free.append([occupied[key][0], occupied[key][1]])
                    free.sort(key=lambda x: x[0])
                    occupied[key][0] = free_range[0]
                    occupied[key][1] = free_range[0] + occupied_len - 1
                    if free_len == occupied_len:
                        free.pop(i)
                    else:
                        free_range[0] += occupied_len
                    break
            for i in range(len(free)-1):
                if free[i][1] == free[i+1][0]:
                    free[i+1][0] = free[i][0]
                    free.pop(i)
    ans = 0
    for key in occupied:
        for i in range(occupied[key][0], occupied[key][1] + 1):
            ans += key * i
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))
