a=["{","}","(",")"]
for x in a:
    if x in ["(",")","{","}"]:
        print("found the match")
        break
    else:
        print("not found")