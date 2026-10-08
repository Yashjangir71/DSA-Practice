#Bubble sort

a = [5, 2, 8, 1]
n = len(a)
for i in range(n):            # one pass per round
    for j in range(n - 1):    # walk through neighbors
        if a[j] > a[j + 1]:   # wrong order?
            a[j], a[j + 1] = a[j + 1], a[j]   # swap them
print(a)  # [1, 2, 5, 8]



#is sorted check
a = [1, 2, 5, 8]
n = len(a)
is_sorted = True
for j in range(n - 1):
    if a[j] > a[j + 1]:
        is_sorted = False
        break
print(is_sorted)  # True

