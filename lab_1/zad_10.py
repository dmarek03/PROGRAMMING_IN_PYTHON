"""
10. Proszę napisać funkcję equivalence(expr1,expr2) sprawdzającą tożsamość dwóch wyrażeń logicznych
w wersji rozszerzonej.
Na przykład:
equivalence(‘a>b’,’~a|b’) -> True
equivalence(‘a>b’,’~a&b’) -> False
"""
from zad_4 import onp
from zad_5 import map
from zad_6 import gen
from zad_7 import val
from zad_8 import count_variable_in_expr


def equivalence(expr1: str, expr2: str) -> bool:
    onp_expr1 = onp(expr1)
    onp_expr2 = onp(expr2)

    possible_variables = gen(count_variable_in_expr(onp_expr1))
    print(f'{possible_variables=}')

    for pv in possible_variables:

        print(f'{map(onp_expr1, pv)=}')
        print(f'{map(onp_expr2, pv)=}')
        print(f'{val(map(onp_expr1, pv))=}')
        print(f'{val(map(onp_expr2, pv))=}')
        if val(map(onp_expr1, pv)) != val(map(onp_expr2, pv)):
            return False
    return True


if __name__ == '__main__':
    # print(equivalence("a>b", "~a|b"))
    # print(equivalence("a>b", "~a&b"))
    #print(equivalence("~(~a|~b)", "a&b"))
    #print(equivalence("~a|~~b", "a>b"))
    #print(equivalence("(p/q)/(p/q)", "p&q"))
    #print(equivalence("(a&~b)|(~a&b)", "a^b"))
    print(equivalence("a|~a&(b|~b)|F", "T"))
