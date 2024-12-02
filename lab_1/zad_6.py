"""
6. Proszę napisać funkcję gen(n), generującą wszystkie ciągi zero-jedynkowe o długości n.
"""


def gen(n: int):
    return ['0'*(n-len(bin(i)[2:])) + bin(i)[2:] for i in range(2**n)]


if __name__ == '__main__':

    print(gen(11))
    