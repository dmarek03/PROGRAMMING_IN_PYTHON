#Generator rekurencyjny
def gen(n):
    if n == 0:
        yield ""
    else:
        for c in gen(n-1):
            yield c+'0'
            yield c+'1'


for n in gen(5):
    print(n)