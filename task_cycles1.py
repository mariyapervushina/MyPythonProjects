m, p, n =  int(input()), int(input()), int(input())
pop = m
for i in range(1, n+1):
    print(i, pop)
    pop = pop + pop * (p/100)