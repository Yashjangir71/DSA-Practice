def small_no(nums):
    ans = []
    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count +=1
        ans.append(count)
    return ans
print(small_no([8, 1, 2, 2, 3]))



# my method to find the number of smaller elements than the current element in an array.
def small_no():
    n = [8, 1, 2, 2, 3]
    ans = []

    for num in n:
        count = 0

        for other in n:
            if other < num:
                count += 1

        ans.append(count)

    return ans


print(small_no())