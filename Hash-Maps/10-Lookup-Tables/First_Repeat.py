a = [1,3,2,3,1]
seen = {}
for num in a:
    if num in seen:
        print(num)
        break
    seen[num] = True