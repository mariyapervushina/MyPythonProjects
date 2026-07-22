n, m = int(input()), int(input())
counter = 0
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i + 3 * j + 2 * k == m:
                print(i, ' + 3×', j, ' + 2×', k, ' = ', m, sep='')
                counter += 1
if counter == 0:
    print('При заданных n и m решений не существует.')



