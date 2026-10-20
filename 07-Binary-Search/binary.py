a = [1, 3, 5, 7, 9]
target = 7
left = 0
right = len(a) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if a[mid] == target:
        found = True
        break
    elif a[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
print(found)
