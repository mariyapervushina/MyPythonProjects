import math
n = int(input())
total1 = 0
for i in range(1, n+1):
    total1 += 1 / i
total2 = total1 - math.log(n)
print(total2)


