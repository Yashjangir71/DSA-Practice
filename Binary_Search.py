a=[1,2,3,4,5]
target=4
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print("Found at index:", mid)
        break
    elif a[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Element not found")