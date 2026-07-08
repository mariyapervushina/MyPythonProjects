n = input()
i = 0
for c in n:
    digit = int(c)
    if digit % 2 == 0:
        i +=1
        print(i, '-я четная цифра равна ', digit, sep='')
if i == 0:
    print('Четных цифр в числе нет')
