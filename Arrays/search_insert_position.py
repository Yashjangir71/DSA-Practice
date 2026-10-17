# The question: You have a sorted row of numbers: [1, 3, 5, 6]. A new number arrives. Where does it sit so the row stays sorted?

# Target 5 → already sitting at index 2. Answer: 2.
# Target 2 → not in the row. It belongs between 1 and 3. Answer: 1.
# Target 7 → bigger than everything, goes at the end. Answer: 4.
# That's it — "find it, or find where it would go."

# The answer: binary search already does the walking for you. When it doesn't find the number, left stops exactly at the empty seat:
a = [1, 3, 5, 6]
target = 3
left = 0
right = len(a) - 1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == target:
        print(mid)
        break
    elif a[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
else:
    print(left)
