s = input().split()
numbers = []
for x in s:
    numbers.append(int(x))
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)


