myset1, myset2, myset3 = set(input().split()), set(input().split()), set(input().split())
myset4 = myset1 & myset2
myset4.difference_update(myset3)
myset4 = [int(i) for i in myset4]
print(*sorted(myset4, reverse=True))



