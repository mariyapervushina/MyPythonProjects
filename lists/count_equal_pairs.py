numbers = input().split()
counter = 0
for i in range (0, len(numbers)):
    for j in range (i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            counter += 1
print(counter)        



