x = int(input())
x1 = x // 100
x2 = x // 10 % 10
x3 = x % 10
s = x1 + x2 + x3
xmin = min(x1, x2, x3)
xmax = max(x1, x2, x3)
if xmax - xmin == s - (xmax + xmin):
    print('Число интересное')
else:
    print('Число неинтересное')