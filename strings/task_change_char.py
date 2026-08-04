s = input()
old_price = 0
new_price = 0
for c in s:
    old_price += ord(c)
eng = 'eyopaxcETOPAHXCBM'
rus = 'еуорахсЕТОРАНХСВМ'
new_s = s
for i in range(len(eng)):
    new_s = new_s.replace(eng[i], rus[i])
for c in new_s:
    new_price += ord(c)
print(f'Старая стоимость: {old_price * 3}🐝')
print(f'Новая стоимость: {new_price * 3}🐝')