a = [4, 9, 2, 7]
biggest = a[0]
for i in range(1, len(a)):
    if a[i] > biggest:
        biggest = a[i]
print(biggest)  # 9
