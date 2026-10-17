a = [1, 2, 2, 2, 3]
target = 2
left = 0
right = len(a) - 1
first = -1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == target:
        first = mid
        right = mid - 1   # found one — but check left for an earlier one
    elif a[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
print(first)  # 1
