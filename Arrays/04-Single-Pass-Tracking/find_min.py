a=[4,9,2,7]
smallest=a[0]
for i in range(1, len(a)):
    if a[i]<smallest:
        smallest=a[i]
print(smallest)  # 2