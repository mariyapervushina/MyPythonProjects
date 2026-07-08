n = int(input())
same = True
last_digit = n % 10
while n != 0:    
    new_last_digit = n % 10
    if last_digit != new_last_digit:
        same = False
    n //= 10    
if same == True:
    print('YES')
else:
    print('NO')

