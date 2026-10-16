s1="listen"
s2="silent"

count1={}
for i in s1:
    if i in count1:
        count1[i]+=1
    else:
        count1[i]=1
count2={}
for i in s2:
    if i in count2:
        count2[i]+=1
    else:
        count2[i]=1
print(count1==count2)