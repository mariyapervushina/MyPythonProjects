# объявление функции
def get_last_index(data, value):
    max_index = 0
    for i in range(len(data)):
        if data[i] == value:
            max_index = i
    if value not in data:
        return 'ERROR!'
    return max_index        

# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))