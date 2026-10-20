a = [3, 1, 2]
result = True
for j in range(len(a) - 1):
    if a[j] > a[j + 1]:
        result = False
        break
print(result)  # False
