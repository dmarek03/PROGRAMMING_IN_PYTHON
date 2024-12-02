"""
8. Proszę napisać funkcję tautology(expr), sprawdzająca czy wyrażenie expr jest tautologią.
Na przykład:
tautology (‘a>a’) -> True
tautology (‘a>(b&c)’) -> False
"""
import string
from zad_4 import onp
from zad_5 import map
from zad_6 import gen
from zad_7 import val


def count_variable_in_expr(expr: str) -> int:
    cnt = 0
    for e in list(set(expr)):
        if e in string.ascii_lowercase and e not in "ft":
            cnt += 1
    return cnt


def tautology(expr: str) -> bool:
   onp_expr = onp(expr)
   possible_values = gen(count_variable_in_expr(onp_expr))

   for pv in possible_values:
       if not val(map(onp_expr, pv)):
           return False
   return True


if __name__ == '__main__':
    # print(tautology("a>a"))
    # print(tautology("a>(b&c)"))
    print(tautology("a|~a&(b|~b)|F"))
