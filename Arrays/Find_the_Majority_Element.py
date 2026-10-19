a = [2, 2, 1, 2, 3]
counts = {}
for num in a:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num in counts:
    if counts[num] > len(a) // 2:
        print(num)
        break
