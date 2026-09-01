# объявление функции
def print_symbol_counts(s):
    counter = 0
    s_list = list(s.lower())
    unique = []
    for c in s_list:
        if c not in unique:
            unique.append(c)
    for c in sorted(unique):
        counter = s_list.count(c)
        print(c, ': ', counter, sep ='')
        
        
# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)