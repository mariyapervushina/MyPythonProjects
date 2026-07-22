a, b = int(input()), int(input())
max_num = 0
max_sum = 0
for i in range(a, b+1):
    total = 0
    for j in range(1, i+1):
        if i % j == 0:
            total += j
    if total >= max_sum:
        max_sum = total
        max_num = i
print(max_num, max_sum)


