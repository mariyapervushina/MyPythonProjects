max_total = 0
word = ''
for _ in range(4):
    s = input()
    total = 0
    for c in s:
        total += ord(c)
    if total > max_total:
        max_total = total
        word = s
print(word)
