def reverse_list(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
print(reverse_list([1, 2, 3, 4, 5]))


# brute force method
# a=[1,2,3,4,5]
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):

#         a[i], a[j] = a[j], a[i]
# print(a)