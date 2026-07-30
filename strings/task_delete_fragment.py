s = input()
first_slice = s[:s.find('h')]
second_slice = s[s.rfind('h')+1:]
print(first_slice, second_slice, sep = '')



