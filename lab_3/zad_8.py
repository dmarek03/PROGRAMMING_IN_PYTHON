# Kolejne pary liczb bliźniaczych -> liczby pierwsze, których różnica wynosi 2

def prime():
    n = 2
    lp =[2]
    yield 2
    while True:
        n += 1
        for p in lp:
            if n % p == 0:
                break
        else:
            lp.append(n)
            yield n


def twins():
    g = prime()
    a = next(g)
    while True:
        b = next(g)
        if b - a == 2:
            yield a, b
        a = b


for twin in twins():
    print(twin)