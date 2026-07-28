n = int(input())
result = ''
last_digit = 0
while n != 0:
    last_digit = n % 2
    result = str(last_digit) + result
    n //= 2
print(result)

