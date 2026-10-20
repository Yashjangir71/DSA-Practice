a = [4, 9, 2, 7]
biggest = a[0]
second = a[0]
for i in range(1, len(a)):
    if a[i] > biggest:
        second = biggest      # old champ slides down
        biggest = a[i]
    elif a[i] > second and a[i] != biggest:
        second = a[i]
print(second)  # 7
# ----------------------------------------------------
# my solution
a = [4, 9, 2, 7]
biggest = a[0]
for i in range(1, len(a)):
    if a[i] > biggest:
        biggest = a[i]

a.remove(biggest)
biggest = a[0]
for i in range(1, len(a)):
    if a[i] > biggest:
        biggest = a[i]
print(biggest)  # 7