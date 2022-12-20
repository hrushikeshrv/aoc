import sys
sys.setrecursionlimit(20000)

with open('inputs/input-20.txt', 'r') as file:
    numbers = list(map(lambda x: int(x), file.readlines()))

# numbers = [1, 2, -3, 3, -2, 0, 4]


def update_idx_of(idx, index_list, delta):
    for i in range(len(index_list)):
        if index_list[i][1] == idx:
            index_list[i][1] += delta
            return


def move(nums, i, n, index_list):
    # print(nums)
    if n == 0:
        return nums
    # print(f'Moving {nums[i]} from {i} to {"left" if n < 0 else "right"}')
    if n > 0:
        if i == len(nums) - 1:
            for j in range(1, i):
                update_idx_of(j, index_list, 1)
            update_idx_of(i, index_list, 2-len(nums))
            nums = [nums[0]] + [nums[i]] + nums[1:i]
            return move(nums, 1, n-1, index_list)
        else:
            update_idx_of(i+1, index_list, -1)
            update_idx_of(i, index_list, 1)
            nums[i+1], nums[i] = nums[i], nums[i+1]
            return move(nums, i+1, n-1, index_list)
    else:
        if i == 0:
            for j in range(1, len(nums)-1):
                update_idx_of(j, index_list, -1)
            update_idx_of(0, index_list, len(nums)-2)
            # print(f'Wrapped {nums[i]}. Was {nums} ', end='')
            nums = nums[1:len(nums)-1] + [nums[0]] + [nums[-1]]
            # print(f'Now {nums}')
            return move(nums, len(nums)-2, n+1, index_list)
        else:
            update_idx_of(i-1, index_list, 1)
            update_idx_of(i, index_list, -1)
            nums[i], nums[i-1] = nums[i-1], nums[i]
            return move(nums, i-1, n+1, index_list)


def solve1(nums):
    nums_idx = [[nums[i], i] for i in range(len(nums))]
    for i in range(len(nums_idx)):
        n, n_idx = nums_idx[i]
        # print(f'\n\nMoving {n}')
        dest = n_idx + n
        if dest < 0:
            dest += len(nums) - 1
        if dest >= len(nums):
            dest = dest % len(nums)
        # print(f'{n} will be moved to index {dest}')
        nums = move(nums, n_idx, n, nums_idx)
        # print(f'Numbers array now becomes {nums}')
    
    idx = nums.index(0)
    return sum(nums[(idx + i) % len(nums)] for i in [1000, 2000, 3000])


# print(solve1(numbers))
