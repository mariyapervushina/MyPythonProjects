pets = [
    ('Freddie', 'Jessica', 'Brown', 38),
    ('Freya', 'Jessica', 'Brown', 38),
    ('Chernysh', 'Harry', 'Wonn', 20),
    ('Kesha', 'Harry', 'Wonn', 20),
    ('Patrick', 'Hermann', 'Schulz', 72),
    ('Foxya', 'Julia', 'Alikina', 47),
    ('Thomas', 'Julia', 'Alikina', 47),
    ('Mia', 'Nikolai', 'Lagunov', 39),
    ('Rufus', 'Harry', 'Wonn', 20),
]
mydict = {}
for name, owner_name, owner_surname, age in pets:
    key = (owner_name, owner_surname, age)
    mydict.setdefault(key, [])
    mydict[key].append(name)
print(mydict)


