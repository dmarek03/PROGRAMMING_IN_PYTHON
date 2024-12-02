#Przekazywanie danych do generatora
from time import (sleep)
def gen(start):
    i = start
    delay = 1.0
    while True:
        new_delay = yield i
        if new_delay:
            delay = new_delay
        if i==0:
            return
        i -= 1
        sleep(delay)

g = gen(30)
for x in g:
    print(x)
    if x == 15:
        # wstrzykujemy wartość do generatora
        print(g.send(0.2))