from collections import Counter
import functools

with open("inputs/input-07.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def compare_hands(hand1, hand2):
    counts_1 = list(dict(Counter(hand1)).values())
    counts_2 = list(dict(Counter(hand2)).values())
    counts_1.sort(reverse=True)
    counts_2.sort(reverse=True)

    if counts_1[0] > counts_2[0]:
        return 1
    elif counts_1[0] < counts_2[0]:
        return -1
    else:
        if counts_1 == [3, 2] and counts_2 == [3, 1, 1]:
            return 1
        elif counts_1 == [3, 1, 1] and counts_2 == [3, 2]:
            return -1
        elif counts_1 == [2, 2, 1] and counts_2 == [2, 1, 1, 1]:
            return 1
        elif counts_1 == [2, 1, 1, 1] and counts_2 == [2, 2, 1]:
            return -1
        hand1 = (
            hand1.replace("J", "U")
            .replace("Q", "V")
            .replace("K", "W")
            .replace("A", "X")
        )
        hand2 = (
            hand2.replace("J", "U")
            .replace("Q", "V")
            .replace("K", "W")
            .replace("A", "X")
        )
        if hand1 > hand2:
            return 1
        elif hand2 > hand1:
            return -1
    return 0


def compare_hands_2(hand1, hand2):
    counts1 = dict(Counter(hand1))
    counts2 = dict(Counter(hand2))
    max_1 = 0
    max_key = ""
    for key in counts1:
        if counts1[key] > max_1 and key != "J":
            max_1 = counts1[key]
            max_key = key
    if max_key and "J" in counts1:
        counts1[max_key] += counts1["J"]
        del counts1["J"]

    max_2 = 0
    max_key = ""
    for key in counts2:
        if counts2[key] > max_2 and key != "J":
            max_2 = counts2[key]
            max_key = key
    if max_key and "J" in counts2:
        counts2[max_key] += counts2["J"]
        del counts2["J"]

    counts1 = list(counts1.values())
    counts2 = list(counts2.values())
    counts1.sort(reverse=True)
    counts2.sort(reverse=True)

    if counts1[0] > counts2[0]:
        return 1
    elif counts1[0] < counts2[0]:
        return -1
    else:
        if counts1 == [3, 2] and counts2 == [3, 1, 1]:
            return 1
        elif counts1 == [3, 1, 1] and counts2 == [3, 2]:
            return -1
        elif counts1 == [2, 2, 1] and counts2 == [2, 1, 1, 1]:
            return 1
        elif counts1 == [2, 1, 1, 1] and counts2 == [2, 2, 1]:
            return -1
        hand1 = (
            hand1.replace("J", "1")
            .replace("Q", "V")
            .replace("K", "W")
            .replace("A", "X")
        )
        hand2 = (
            hand2.replace("J", "1")
            .replace("Q", "V")
            .replace("K", "W")
            .replace("A", "X")
        )
        if hand1 > hand2:
            return 1
        elif hand2 > hand1:
            return -1
    return 0


def solve1(lines):
    cmp = functools.cmp_to_key(lambda x, y: compare_hands(x.split()[0], y.split()[0]))
    lines.sort(key=cmp)
    # print(lines)
    score = 0
    for idx, line in enumerate(lines):
        score += (idx + 1) * int(line.split()[1])
    return score


def solve2(lines):
    cmp = functools.cmp_to_key(lambda x, y: compare_hands_2(x.split()[0], y.split()[0]))
    lines.sort(key=cmp)
    # print(lines)
    score = 0
    for idx, line in enumerate(lines):
        score += (idx + 1) * int(line.split()[1])
    return score


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
