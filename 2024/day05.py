with open('inputs/input-05.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))
    orderings_ = {}
    updates_ = []
    for line in input_:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            _ = line.split('|')
            if _[0] not in orderings_:
                orderings_[_[0]] = []
            orderings_[_[0]].append(_[1])
        else:
            updates_.append(line.split(','))


def solve1(updates, orderings):
    ans = 0
    for update in updates:
        seen = set()
        valid = True
        for num in update:
            if not valid:
                break
            for prev in orderings.get(num, []):
                if prev in seen:
                    valid = False
                    break
            seen.add(num)
        if valid:
            ans += int(update[len(update)//2])
    return ans


def find_right_idx(update, orderings, num):
    prevs = set(x for x in orderings[num] if x in update)
    for i, num in enumerate(update):
        if num in prevs:
            return i
    return len(update) - 1


def find_violation_idx(update, orderings):
    seen = set()
    for i, num in enumerate(update):
        for prev in orderings.get(num, []):
            if prev in seen:
                return i
        seen.add(num)
    return -1


def solve2(updates, orderings):
    ans = 0
    for update in updates:
        invalid_idx = find_violation_idx(update, orderings)
        invalid = invalid_idx >= 0
        while invalid_idx >= 0:
            right_idx = find_right_idx(update, orderings, update[invalid_idx])
            update.insert(right_idx, update.pop(invalid_idx))
            invalid_idx = find_violation_idx(update, orderings)
        if invalid:
            ans += int(update[len(update)//2])
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(updates_, orderings_))
    print(solve2(updates_, orderings_))

