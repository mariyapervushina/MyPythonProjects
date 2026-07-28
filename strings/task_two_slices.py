s = input()
border = (len(s) + 1) // 2
s_first = s[:border]
s_last = s[border:]
print(s_last + s_first)


