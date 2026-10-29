wordlist = input().split()
wordset = set(wordlist[0])
is_same = True
for word in wordlist[1:]:
    new_wordset = set(word)
    if wordset != new_wordset:
        is_same = False
if is_same:
    print('YES')
else:
    print('NO')

