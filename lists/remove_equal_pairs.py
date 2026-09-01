n = int(input())
words = []
new_words = []
for i in range(n):
    words.append(input())
for word in words:
    if word not in new_words:
        new_words.append(word)
print(*new_words, sep = '\n')

