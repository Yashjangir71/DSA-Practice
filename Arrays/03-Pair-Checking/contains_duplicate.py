a = [1, 2, 3, 1]
found = False
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print("Duplicate found:", a[i])
            found = True
            break
    if found:
        break
print(found)
