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
