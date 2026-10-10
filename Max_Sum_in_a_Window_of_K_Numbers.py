a = [1, 4, 2, 10, 3]
k = 3

window_sum = 0
for i in range(k):        # add up the first window
    window_sum += a[i]
max_sum = window_sum

for i in range(k, len(a)):            # i = entering position
    window_sum = window_sum - a[i - k] + a[i]   # drop the back, add the front
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)  # 16
