"""
3. Proszę napisać funkcję bal(exp,op), zwracającą najbardziej prawą pozycję danego operatora
niezagnieżdżonego w nawiasach.
Na przykład:
bal(‘a>(b>c)’,’>’) -> 1
bal(‘a|b&c’,’&’) -> 3
bal(‘a|(b&c’),’&’) -> None
"""


def bal(expr: str, ops: str) -> int | None:
    cnt = 0

    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ')':
            cnt += 1
        elif expr[i] == '(':
            cnt -= 1

        elif expr[i] in ops and cnt == 0:
            return i
    return None


if __name__ == '__main__':
    print(bal("a>(b>c)", ">"))
    print(bal("a|b&c", "&"))
    print(bal("a|(b&c", "|"))
    print(bal("~b", "~^&|/>"))


