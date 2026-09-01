ip = input().split('.')
is_correct = True
for num in ip:
    if int(num) > 255:
        is_correct = False
if is_correct:
    print('ДА')
else:
    print('НЕТ')



