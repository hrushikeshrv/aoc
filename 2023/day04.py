with open("inputs/input-04.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve1(cards):
    score = 0
    for card in cards:
        winning = set(card.split(":")[1].split("|")[0].strip().split())
        nums = set(card.split(":")[1].split("|")[1].strip().split())
        value = 0
        for num in nums:
            if num in winning:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        score += value
    return score


def solve2(cards):
    score = 0
    n_cards = {x: 1 for x in range(len(cards))}
    for i in range(len(cards)):
        card = cards[i]
        winning = set(card.split(":")[1].split("|")[0].strip().split())
        nums = set(card.split(":")[1].split("|")[1].strip().split())
        matches = len(nums.intersection(winning))
        for j in range(1, matches + 1):
            n_cards[i + j] += n_cards[i]
    for card in n_cards:
        score += n_cards[card]
    return score


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
