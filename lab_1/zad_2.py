"""
2. Proszę napisać funkcję bracket(expr) usuwającą w wyrażeniu zewnętrzne nawiasy.
Na przykład:
‘(a|b)’ -> ‘a|b’
‘((a>b)&(c>d))’ -> ‘(a>b)&(c>d)’
‘(((a)))’ -> ‘a’
"""
from zad_1 import check


def bracket(expr: str) -> str:
    if len(expr) < 3:
        return expr
    return bracket(expr[1:-1]) if expr[0] + expr[-1] == '()' and check(expr[1:-1]) else expr


if __name__ == '__main__':

    print(bracket("(((a)))"))
    print(bracket("(a>b)>c"))
    print(bracket("(~a|~b)"))
    print(bracket("(a|b)|((c|a)|b)"))
    print(bracket("((c|a)|b)"))

