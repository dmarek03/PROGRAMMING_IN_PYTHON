"""
9. Proszę napisać funkcję alg(expr) zamieniającą wyrażenie z postaci ONP na postać algebraiczną
Na przykład:
alg(‘ab&’) -> ‘a&b’
alg(‘ab>c>’) -> ‘a>b>c’
alg(‘abc|>’) -> ‘a>(b|c)’
"""
import string
from zad_4 import onp
from zad_2 import bracket

def get_priority(operator: str) -> int:
    priorities = {
        '~': 4,
        '^': 3,
        '&': 2,
        '|': 2,
        '/': 2,
        '>': 1
    }
    return priorities.get(operator, 0)

def find_last_operand_priority(expr: str) -> int:
    operators = {'/', '~', '|', '^', '&', '>'}
    for e in expr[::-1]:
        if e in operators:
            return get_priority(e)
    return -1



def alg(expr: str) -> str:
    st = []
    for e in expr:
        if e in string.ascii_lowercase and e not in "tf":
            st.append(e)

        if e =="~" and len(st) > 0:
            first_var = st.pop()
            st.append("("+e+first_var+")")
        elif e in "^/&>|":
            second_var = st.pop()
            first_var = st.pop()
            st.append("("+first_var+e+second_var+")")

    return bracket(st[0])


if __name__ == '__main__':
    print(alg("ab&"))
    print(alg("ab>c>"))
    # print(alg("abc|>"))
    # print(alg("a~b~|~"))
    # print(alg("ab|ca|b||"))
    # print(alg("a~b|"))
    # print(alg("pq/pq//"))
    # print(alg("ab~&a~b&|"))
    # print(alg(onp("a|b|c")))
    #print(alg('pqr|&pq&>r|'))
    print(alg(onp("b^a>d")))

