# Binary Search Implementation
a=[1,2,3,4,5]
target=4
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print("Found at index:", mid)
        break
    elif a[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Element not found")


# Search Insert Position
def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4
print(search_insert([1, 3, 5, 6], 0))  # 0
