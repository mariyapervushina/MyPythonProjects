n = int(input())
char_set = set()
for _ in range(n):
    char_set.update(input().lower())   
print(len(char_set))


