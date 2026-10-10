a=[1,4,2,10,3]
k=3
max_sum=0
for i in range(len(a)-k+1):
    current_sum=sum(a[i:i+k])
    if current_sum>max_sum:
        max_sum=current_sum
print(max_sum)