a = "madam"
i = 0
j = len(a) - 1
while i < j:
    if a[i] != a[j]:
        print("Not a palindrome")
        break
    i += 1
    j -= 1
else:
    print("Is a palindrome")
