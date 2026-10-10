char_list = []
a = []
for char in input().split():
    if a == []:
        a.append(char)
    else:
        if a[-1] == char:
            a.append(char)
        else:
            char_list.append(a)
            a = [char]
if a != []:
    char_list.append(a)
print(char_list)

