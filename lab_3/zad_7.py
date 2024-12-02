# Kolejne liczby pierwsze


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

for n in prime():
    print(n)