import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d == 0:
    print(- (b / (2 * a)))
elif d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    if x1 <= x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
else:
    print('Нет корней')



