#Two Sum
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(two_sum([2, 7, 11, 15], 9))


# contains_duplication(bonus)
def contains_duplication(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False    
print(contains_duplication([1, 2, 3, 4, 5]))