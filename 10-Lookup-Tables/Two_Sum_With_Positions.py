a = [2, 7, 5, 4, 15]
target = 9
seen = {}
for i in range(len(a)):
    need = target - a[i]
    if need in seen:
        print(seen[need], i)
        break
    seen[a[i]] = i
