a = [1, 12, -5, -6, 50, 3]
k = 4
best = 0
for i in range(len(a) - k + 1):
    total = 0
    for j in range(i, i + k):
        total += a[j]
    if total > best:
        best = total
print("best average:", best / k)
