a = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
best = 9999
for i in range(len(a) - k + 1):
    total = 0
    for j in range(i, i + k):
        total += a[j]
    if total < best:
        best = total

print("min sum :", best)
