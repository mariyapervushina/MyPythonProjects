n = int(input())
students = [tuple(input().split()) for _ in range(n)]
good_st = []
for t in students:
    if int(t[-1]) >= 4:
        good_st.append(t)    
for row in students:
    print(*row)
print()
for row in good_st:
    print(*row)