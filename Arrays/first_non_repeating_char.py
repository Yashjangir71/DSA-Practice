s="aabbc"
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in count:
    if count[i]==1:
        print(i)
        break