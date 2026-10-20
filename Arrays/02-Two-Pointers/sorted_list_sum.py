a=[1,2,3,4,5]
target=9
i=0
j=len(a)-1
found=False
while i<j:
    s=a[i]+a[j]
    if s==target:
        print("Pair found:", a[i], a[j])
        found=True
        break
    elif s<target:
        i+=1
    else:
        j-=1
print(found)