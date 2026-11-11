a = [i for i in input().lower() if i not in '.,!?:;- ']
b = [i for i in input().lower() if i not in '.,!?:;- ']
if sorted(a) == sorted(b):
    print('YES')
else:
    print('NO')



