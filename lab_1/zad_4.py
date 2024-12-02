"""
4. Proszę napisać funkcję onp(expr) zamieniającą wyrażenie z postaci algebraicznej (infiksowej) na postać ONP
(postfiksową).
Na przykład:
onp(‘a&b’) -> ‘ab&’
onp( ‘a>b>c’) -> ‘ab>c>’
onp( ‘(a>(b|c))’) -> ‘abc|>’
"""
from zad_1 import remove_double_negations, remove_spaces
from zad_2 import bracket
from zad_3 import bal


def onp(expr):
    expr = remove_double_negations(expr)
    expr = remove_spaces(expr)
    expr1 = bracket(expr)
    #print(f'{expr1=}')
    if p := bal(expr1, '^&|/>'):
        return onp(expr1[:p]) + onp(expr1[p + 1:]) + expr1[p]
    p = bal(expr1, "~")
    if p is not None:
        return onp(expr1[p + 1:]) + expr1[p]

    return expr


if __name__ == '__main__':
    # print(onp("~~a&b"))
    # print(onp("~a>b>c"))
    # print(onp("(a>(b|c))"))
    # print(onp("~(~a|~b)"))
    print(onp("(a|b)|(c|a|b)"))
    print(onp("~(~a|~b)"))
    print(onp("~a|~~b"))
    print(onp("(p/q)/(p/q)"))
    print(onp("(a&~b)|(~a&b)"))
    print(onp("a|~a&(b|~b)|F"))

