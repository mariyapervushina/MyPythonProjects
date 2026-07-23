n = int(input())
for h in range(0, 24):
    for m in range(0, 60):
        if h ** n == m:
            hs = str(h)
            if h < 10:
                hs = '0' + str(h)
            ms = str(m)
            if m < 10:
                ms = '0' + str(m)
            print(hs, ':', ms, sep='')



