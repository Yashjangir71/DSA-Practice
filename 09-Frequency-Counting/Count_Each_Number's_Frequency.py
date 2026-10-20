a = [1, 2, 2, 3]
counts = {}
for num in a:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)
