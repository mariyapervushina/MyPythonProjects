n = int(input())
citydict = {}
for _ in range(n):
    words = input().split()
    country = words[0]
    cities = words[1:]
    for city in cities:
        citydict[city] = country
for _ in range(int(input())):
    print(citydict[input()])