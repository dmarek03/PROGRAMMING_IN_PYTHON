"""
5. Proszę napisać funkcje map(expr, vec) mapującą zmienne w wyrażeniu ONP na wartości z wektora vec.
Można założyć, że długość wektora vec jest równa liczbie zmiennych w wyrażeniu.
Na przykład:
map(‘ab&c|’,’101’) -> ‘10&1|’
map(‘ac>b>’,’101’) -> ‘11>0>|’

"""
import string


def map(expr, vec):
    if expr == "F":
        return "0"
    if expr == "T":
        return "1"
    t = {sorted(list(set(expr).intersection(set(string.ascii_lowercase))))[i]: vec[i] for i in range(len(vec)) if vec[i] not in "ft"}
    print(string.ascii_lowercase)
    print(f'{t=}')
    for k in t:
        expr = expr.replace(k, t[k])
    return expr


if __name__ == '__main__':

    print(map("ab&c|", "101"))
    print(map("ac>b>", "101"))
    print(map("a~b|~", "01"))
    print(map("aa~|bb~|&F|", "01"))
