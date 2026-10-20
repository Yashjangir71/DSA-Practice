a = [2,7,5,4,15]
target = 9
seen = {}
for num in a:
    need = target - num
    if need in seen:
        print([need, num])
    seen[num] = True