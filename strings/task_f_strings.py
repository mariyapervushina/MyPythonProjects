day = int(input())
weight = float(input())
goal = 100 - 0.2 * day
if weight <= goal:
    print('Все идет по плану')
else:
    print('Что-то пошло не так')
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal} кг')

