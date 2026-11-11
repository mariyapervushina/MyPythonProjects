mydict = {}
result = []
ids = input().split()
for ident in ids:
    mydict.setdefault(ident, 0)
    mydict[ident] += 1
    if mydict[ident] == 1:
        result.append(ident)
    else:
        ident_ = f'{ident}_{mydict[ident] - 1}'
        result.append(ident_)
print(*result)        