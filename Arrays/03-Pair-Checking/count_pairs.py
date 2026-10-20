a=[1,2,3,4,5]
target=6
count=0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            count += 1
print(count)
