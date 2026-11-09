text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
result = {}
for char in text:
    result.setdefault(char, 0)
    result[char] += 1
print(result)




