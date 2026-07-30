s = input()
letters = 'АВЕКМНОРСТУХ'
if len(s) != 9 and len(s) != 10:
    print('NO')
elif (s[0] in letters and s[1:4].isdigit() and s[4] in letters and s[5] in letters and s[6] == '_' and s[7:].isdigit()):
    print('YES')
else:
    print('NO')