def find_odd_numbers(low, high):
    return [(high +1)//2 - (low)//2]
print(find_odd_numbers(1, 10))



## Second method
def find_odd_numbers(low, high):
    odd_numbers = []
    for num in range(low, high + 1):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
print(find_odd_numbers(1, 10))