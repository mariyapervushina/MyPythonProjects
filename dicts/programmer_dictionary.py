n = int(input())
mydict = {}
for _ in range (n):
    word, definition = input().split(': ', 1)
    mydict[word.lower()] = definition
m = int(input())
for _ in range(m):
    print(mydict.get(input().lower(), 'Не найдено'))

