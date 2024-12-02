# Generatora a funkcja generująca
def podz(n):
    for p in range(1,n):
        if n%p==0:
            yield p
g=podz(24)
print(g)

next(g)

next(g)

