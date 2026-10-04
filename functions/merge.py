# объявление функции
def merge(list1, list2):
    numbers3 = numbers1 + numbers2
    numbers3.sort()
    return numbers3

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))