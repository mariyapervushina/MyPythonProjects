# объявление функции
def print_case_counts(s):
    count_U = 0
    count_L = 0
    new_s = []
    for syl in s:
        if syl.isalpha():
            new_s.append(syl)
    for syl in new_s:
        if syl == syl.upper():
            count_U += 1
    for syl in new_s:
        if syl == syl.lower():
            count_L += 1
    print(f'Букв в верхнем регистре: {count_U}')
    print(f'Букв в нижнем регистре: {count_L}')

# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)