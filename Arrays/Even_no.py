a = [3, 5, 2, 8]
count = 0
for i in range(len(a)):
    if a[i]%2 == 0:
        count += 1
print("Count of even numbers in the array is:", count)