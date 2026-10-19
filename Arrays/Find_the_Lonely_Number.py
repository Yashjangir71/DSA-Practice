a=[4,1,2,1,2]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for i in count:
    if count[i]==1:
        print(i)
        break
