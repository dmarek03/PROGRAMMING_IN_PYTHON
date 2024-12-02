"""
1. Proszę napisać funkcję check(expr),
sprawdzającą poprawność wyrażenia logicznego.
Na przykład:
‘a>b>c&a’ -> True
‘(a>(b&c)’ -> False
"""
from re import sub
import string


def remove_spaces(exp: str) -> str:
    return sub(" ", "", exp)


def remove_double_negations(expr: str) -> str:
    return sub("~~", "", expr)


def check(expr: str) -> bool:
    operators = '^&|/>'
    variables = string.ascii_lowercase + 'TF'
    state = True
    cnt = 0
    expr = remove_spaces(expr)
    for e in expr:
        if state:
            if e == '(':
                cnt += 1

            elif e in variables:
                state = False

            elif e == "~":
                state = True

            else:
                return False

        else:
            if e == ")":
                cnt -= 1

            elif e in operators:
                state = True

            else:
                return False

        if cnt < 0:
            return False

    return cnt == 0 and not state


if __name__ == '__main__':
    print(remove_spaces("((((~~(~(~a>b)) ) )))"))
    print(check("((((~~(~(~a>b)) ) )))"))
    print(check("a~b"))



