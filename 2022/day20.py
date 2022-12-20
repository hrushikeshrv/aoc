import sys
sys.setrecursionlimit(20000)

with open('inputs/input-20.txt', 'r') as file:
    numbers = list(map(lambda x: int(x), file.readlines()))

# numbers = [1, 2, -3, 3, -2, 0, 4]

numbers = [(numbers[i], i) for i in range(len(numbers))]


def move(nums, start, move_amt, index_map):
    if move_amt == 0:
        return nums
    if move_amt > 0:
        if start == len(nums)-1:
            for j in range(1, start):
                index_map[nums[j]] += 1
            index_map[nums[start]] += 2 - len(nums)
            nums = [nums[0]] + [nums[start]] + nums[1:start]
            return move(nums, 1, move_amt-1, index_map)
        else:
            index_map[nums[start]] += 1
            index_map[nums[start+1]] -= 1
            nums[start], nums[start+1] = nums[start+1], nums[start]
            return move(nums, start + 1, move_amt - 1, index_map)
    else:
        if start == 0:
            for j in range(1, len(nums)-1):
                index_map[nums[j]] -= 1
            index_map[nums[start]] += len(nums) - 2
            nums = nums[1:len(nums)-1] + [nums[0]] + [nums[-1]]
            return move(nums, len(nums)-2, move_amt+1, index_map)
        else:
            index_map[nums[start]] -= 1
            index_map[nums[start-1]] += 1
            nums[start], nums[start-1] = nums[start-1], nums[start]
            return move(nums, start-1, move_amt+1, index_map)


def solve1(nums):
    order = nums[:]
    num_index = {(num, idx): idx for num, idx in order}
    # print(num_index)
    
    for n in order:
        idx = num_index[n]
        # print(f'Moving {n}')
        nums = move(nums, idx, n[0], num_index)
        # print([x[0] for x in nums])
    
    idx = 0
    for i in range(len(nums)):
        if nums[i][0] == 0:
            idx = i
    return sum(nums[(idx + i) % len(nums)][0] for i in [1000, 2000, 3000])


print(solve1(numbers))
