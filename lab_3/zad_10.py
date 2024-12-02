def gen1(n):
    i = 1
    while i <= n:
        yield i
    i += 1

def gen2(ciag_we):
    for x in ciag_we:
        yield x**0.5

for n in gen2(gen1(10)):
    print(n)
print(sum(gen2(gen1(10))))
