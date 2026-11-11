n = int(input())
phonebook = {}
for _ in range(n):
    phone, name = input().split()
    phonebook.setdefault(name.lower(), []).append(phone)    
for _ in range(int(input())): 
    print(*phonebook.get(input().lower(), ['абонент не найден']))


