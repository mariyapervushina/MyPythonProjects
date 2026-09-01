# объявление функции
def print_perm_time_call(msc_time):
    time = msc_time.split(':')
    perm_hour = int(time[0]) + 2
    print(f'Созвон будет в {perm_hour:02d}:{time[1]}.')

# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)