from itertools import combinations
from string import ascii_lowercase
from sympy.logic import simplify_logic
from sympy.abc import a,b,c,d,e,f,g,h,i,j,k

s = ~a|~~b
print(simplify_logic(s))

def join(s1, s2):
    # licznik różnic
    diff_cnt = 0
    w = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            w += s1[i]
        else:
            w += '-'
            diff_cnt += 1

    return w if diff_cnt == 1 else None


# print(lacz('1010','1110'))
# print(lacz('1010','1111'))

def minimize(s):
    s2 = set()
    b1 = False
    for e1 in s:
        b2 = False
        for e2 in s:
            n = join(e1, e2)
            # Jeśli udało się połączyć wektory to
            # wynikowy wektor dodajemy do zbioru
            if n:
                s2.add(n)
                b1 = b2 = True
        # Jeśli wektor z niczym się nie łączy
        # to trafia w orginalnym stanie do zbioru
        if not b2:
            s2.add(e1)

    if b1:
        return minimize(s2)
    else:
        return s2


#s = { '0100','0111','1001','1010','1100','1101','1110','1111' }
# print(s)
# s2 = minimize(s)
# print(s2)


def wyr(s):
    res = ""
    # Przechodzimy przez wszystkie elementy zbiory
    for e in s:
        res2 = ""
        # Itereujemy przez kolejne składowe elementu
        for i in range(len(e)):
            if e[i] == '-':
                continue
            if e[i] == '0':
                res2 += "~"
            res2 += ascii_lowercase[i] + '&'
        # Dokładamy wynikowy iloczyn do głównego resultatu
        res += "(" + res2[:-1] + ")|"

    return res[:-1]

#
# print(wyr(s))
# print(wyr(s2))

# sprawdza czy wektor wejściowy pasuje do zredukowanego wzorca
def match(x, w):
    # Przebiegamy po jednym wektorze
    for i in range(len(w)):
        if w[i] == '-':
            continue
        # Jeśli elementy wzorca i wektora są różne to zwracamy False
        if w[i] != x[i]:
            return False

    return True


# print(match('1010','10--'))
# print(match('1110','-10-'))

# minimalny podzbiór
def minp(d, w):
    # r - wielkość podzbioru
    for r in range(1, len(w)):
        # generujemy kombinacje ze zbioru w
        # wszystkie podzbioru o rozmiarze r
        for c in combinations(w, r):
            nowy = set()
            for el in d:
                for wz in c:
                    # Sprawdzamy czy element pasuje do wzorca,
                    # jeśli tak to dokładamy go do zbioru
                    if match(el, wz):
                        nowy.add(el)
            # sprawdzamy czy rozmiar danych i zbioru jest równy
            if len(nowy) == len(d):
                return c

# print(wyr(s))
# s3 = minp(s, s2)
# print(s3)
# print(wyr(s3))
# s = {"000", "001", "010", "100", "110", "101", "011", "111"}
# x = ('(a|b)|(c|a|b)')
# x2 = minimize(s)
# print(wyr(x2))

