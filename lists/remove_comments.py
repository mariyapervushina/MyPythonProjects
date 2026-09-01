s = list(input())
del s[0]
n = int(''.join(s))
string = ''
for i in range(n):
    string = input()
    if '#' in string:
        string = string[:string.index('#')]
        print(string.rstrip())
    else:
        print(string.rstrip())
              
              


