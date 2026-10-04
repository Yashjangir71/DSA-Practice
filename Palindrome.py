#Two pointer approach to check if a string is a palindrome
a = input("Enter a string: ")
i = 0
j = len(a) - 1
is_palindrome = True
while i < j:
    if a[i] != a[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
print(is_palindrome)


#slicing method to check if a string is a palindrome
a="abca"
k=a[::-1]
print(k)

if a==k:
    print("true")
else:
    print("false")