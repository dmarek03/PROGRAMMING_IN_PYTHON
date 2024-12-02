def podz(n):
    for p in range(1, n):
        if n % p == 0:
            yield p


for i in podz(120):
    print(i)
l = [x for x in podz(24)]
print(l)