a = [2, 7, 11, 15]
target = 9
found = False
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print("Pair found:", a[i], a[j])
            found = True
            break
    if found:
        break
print(found)
