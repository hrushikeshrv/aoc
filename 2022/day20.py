import sys
sys.setrecursionlimit(20000)

with open('inputs/input-20.txt', 'r') as file:
    numbers = list(map(lambda x: int(x), file.readlines()))

numbers = [(numbers[i], i) for i in range(len(numbers))]


def solve1(nums):
    order = nums[:]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if order[j] == nums[i]:
                item = order.pop(j)
                new_index = (j + item[0]) % len(order)
                order.insert(new_index, item)
                break

    idx = 0
    for i in range(len(order)):
        if order[i][0] == 0:
            idx = i
    return sum(order[(idx + i) % len(order)][0] for i in [1000, 2000, 3000])


print(solve1(numbers))

with open('inputs/input-20.txt', 'r') as file:
    numbers = list(map(lambda x: int(x), file.readlines()))
numbers = [(numbers[i] * 811589153, i) for i in range(len(numbers))]


def solve2(nums):
    order = nums[:]
    for _ in range(10):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if order[j] == nums[i]:
                    item = order.pop(j)
                    new_index = (j + item[0]) % len(order)
                    order.insert(new_index, item)
                    break

    idx = 0
    for i in range(len(order)):
        if order[i][0] == 0:
            idx = i
    return sum(order[(idx + i) % len(order)][0] for i in [1000, 2000, 3000])


print(solve2(numbers))
