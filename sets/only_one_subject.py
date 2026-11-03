m, n = int(input()), int(input())
namelist = [input() for _ in range(m + n)]
nameset = set(namelist)

result = 2 * len(nameset) - len(namelist)
if result == 0:
    print('NO')
else:
    print(result)