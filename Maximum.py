##Finding the maximum number in a list using two different approaches.
a = [12, 3, 18, 5]
i = 0
j = i + 1
while j < len(a):
    if a[i] < a[j]:
        a[i] = a[j]
    j += 1
print(a[i])  # 9

##second approach
a=[12, 3, 18, 5]
i=0
j=len(a)-1
while i<=j:
    if a[i]<a[j]:
        i+=1
    else:
        j-=1
print(a[i])  

##find second largest number in a list
a = [4, 9, 2, 7]

# round 1: find the max
i = 0
j = len(a) - 1
while i < j:
    if a[i] < a[j]:
        i += 1
    else:
        j -= 1
first = a[i]

# kick the winner out, round 2: find the max of what's left
a.remove(first)
i = 0
j = len(a) - 1
while i < j:
    if a[i] < a[j]:
        i += 1
    else:
        j -= 1
print(a[i])  # 7
