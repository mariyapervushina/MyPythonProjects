text = 'bridge snake island game glory eye arrogant car nature game glory game'
new_dict = {}
for word in text.split():
    new_dict.setdefault(word, 0)
    new_dict[word] +=1
max_count = max(new_dict.values())
print(min([i for i in new_dict if new_dict[i] == max_count]))



