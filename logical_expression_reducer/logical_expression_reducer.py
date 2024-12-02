# Dominik Marek
"""
1. Wejściem jest wyrażenie logiczne
2. T, F - stałe oznaczające prawde i fałsz
3. Operatory : ~, ^, &, |,/, >

Dane wejściowe:
-ma czytać dane ze standrowego wejścia(nie input)
- czytamy jedno wyrażenie -> redukujemy -> wynik bez ozdobników
- spacje na wejściu należy redukować
- jak mamy niepoprawne wyrażenie to wyświetla ERROR

Redukcja:
-długość wyrażenia ma być mniejsza od wyjściowej
- wyrażenia mają miec ten sam sens logiczny
- jak nie da się zredukować to zwracamy to samo
"""
from re import sub
import string


# Funkcja usuwa spacje z wyrażenia
def remove_spaces(expr: str) -> str:
    return sub(" ", "", expr)

#Funckja usuwa podwójne negacje z wyrażenia
def remove_double_negations(expr: str) -> str:
    return sub("~~", "", expr)


# Funkcja weryfikująca czy dane wyrażenie logiczne jest poprawne.
# Sprawdzamy czy liczba nawiasów otwierających i zamykających jest jednakowa oraz czy wyrażenie składa się przynajmaniej
# z jednej zmiennej oraz operatorów w poprawnych miejscach (flaga state ustawionna na False)
def check(expr: str) -> bool:

    operators = '^&|/>'
    variables = string.ascii_lowercase + 'TF'
    state = True
    cnt = 0
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


def perm(s):
    if len(s) == 1:
        yield s

    else:
        for p in perm(s[1:]):
            for i in range(len(s)):
                yield p[:i] + s[0]+ p[i:]


def comb(text, k):
    if k == 1:
        for t in text:
            yield t

    elif len(text) == k:
        yield text
    else:

        for c in comb(text[1:], k-1):
            yield text[0] + c

        for c in comb(text[1:], k):
            yield c

# Za pomocą funkcji perm i comb generujemy k-elementowe kombinacje bez powtórzeń ze zbioru wejściowego s, które są
# poprawnymi logicznie wyrażeniami
def var(s, k):

    for c in comb(s,k):
        for p in perm(c):
            if check(p) and '~~' not in p:
                yield p

# Funkcja usuwa zbędne zewrzętrzne nawiasy z wyrażenia
def bracket(expr: str) -> str:

    if len(expr) < 3:
        return expr
    return bracket(expr[1:-1]) if expr[0] + expr[-1] == '()' and check(expr[1:-1]) else expr


# Poniższa funkcja znajduje  najbardziej prawą pozycję danego operatora niezagnieżdżonego w nawiasach.
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


# Zamiana wyrażenia z postaci algebraicznej do odwrotnej notacji polskiej
# Najpierw usuwamy podwójne negacje i zbędne nawiasy zewnętrzne z wyrażenia a następnie znajdujemy za pomocą funkcji bal
# najbardziej prawą pozycję danego operatora niezagnieżdżonego w nawiasach. Jeśli jest to operator negacji to zwracamy
# onp(expr[p+1] + expr[p], gdzie p to indeks znaleziony za pomocą funkcji bal. Jeśli mamy do czynienia z innym operatorem
# to zwracamy dodatkowo człon onp(expr1[:p]) - czyli wywołanie rekurencjne dla frgamentu wyrażenia przed danym operatorem.

def onp(expr):

    expr = remove_double_negations(expr)
    expr1 = bracket(expr)

    if p := bal(expr1, '^&|/>'):
        return onp(expr1[:p]) + onp(expr1[p + 1:]) + expr1[p]
    p = bal(expr1, "~")
    if p is not None:
        return onp(expr1[p + 1:]) + expr1[p]

    return expr


# Funckja mapującą zmienne w wyrażeniu ONP na wartości z wektora vec
def map(expr, vec):

    if expr == "F":
        return "0"
    if expr == "T":
        return "1"
    t = {sorted(list(set(expr).intersection(set(string.ascii_lowercase))))[i]: vec[i] for i in range(len(vec)) if vec[i] not in "ft"}

    for k in t:
        expr = expr.replace(k, t[k])
    return expr

# Funkcja genreuje wszytskie ciągi zer i jedynek o długośći n
def gen(n):
    if n == 0:
        yield ""
    else:
        for c in gen(n-1):
            yield c+'0'
            yield c+'1'

# Za pomocą funkcji val sprawdzamy wartość wyrażenia podanego jako wcześniej zapowane wyrażenie postaci ONP na dany
# wektor zbudowany z zer i jedynek. Wartość danego wyrażenia uzysukjemy następująco:
# 1) Jeśli dany znak z wyrażenia jest O,1,T,F to dodajemy odpowiednią wartość zero albo jeden na stos
# 2) Jeśli natrafimy na operator to pobieramy jedną albo dwie wartośći i obliczamy wartość wyrażenia w zależności od
# własności operatora a wynik tej operacji dodajemy na stos
# 3) Finalnie zwracamy ostatni element ze stosu co jest tożsame z wartością wyrażenia wejściowego
def val(expr):

    st = []
    for e in expr:

        if e in '01TF':
            if e in "1T":
                st.append(1)

            else:
                st.append(0)


        elif e == '|':
            second_var = st.pop()
            first_var = st.pop()

            st.append(first_var or second_var)


        elif e == '&':
            second_var = st.pop()
            first_var = st.pop()

            st.append(first_var and second_var)


        elif e == '>':
            second_var = st.pop()
            first_var = st.pop()

            st.append((1-first_var) or second_var)


        elif e == "^":
            second_var = st.pop()
            first_var = st.pop()
            st.append(((first_var or second_var) and (1-(first_var and second_var))))

        elif e == "/":
            second_var = st.pop()
            first_var = st.pop()
            st.append(1-(first_var and second_var))

        elif e == '~':
            first_var = st.pop()
            st.append(1-first_var)


        else:
            break
    return st.pop()


# Funkcja znajuduje zmienne w podanym wyrażeniu
def find_variable_in_expr(expr: str) -> str:
    variables = ''

    for e in list(set(expr)):
        if e in string.ascii_lowercase and e not in "ft":
            variables += str(e)

    return variables

# Funkcja znajduje operatory w danym wyrażeniu
def find_operands_in_expr(expr: str) -> str:
    operands = ''

    for e in list(expr):
        if e in "~/^|>&":
            operands += str(e)

    return operands

# Dzięki poniższej funkcji możemy sprawdzić czy dane wyrażenie jest tautologią , czyli czy dla dowolnego wartościowania
# zmienych jest ono zawsze prawdziwe bądź zawsze fałszywe. Sprawdzamy to następująco:
# 1) Przedstawiamy wyrażenie w postaci ONP
# 2) Generujemy wszytskie ciągi zer i jedynek o długości równej liczbie zmienncyh w naszym wyrażeniu
# 3) Iterujemy przez wygenerowane ciągi i sprawdzamy wartośći naszego wyrażenia dla postaci ONP zmapowanej na dany ciag
# 4) Uzyskaną wartość dodajemy do tablicy i sprawdzamy czy poprzednia wartość była taka sama jeśli nie to zwracamy False
# 4) Jeśli wszytskie wartośći w tablicy są takie same to zwracamy odpowiednio 'T' albo 'F' w zależności od zwartości tablicy
def tautology(expr: str) -> bool| str:
    onp_expr = onp(expr)

    n = len(find_variable_in_expr(onp_expr))
    possible_values = gen(n)
    tab = []
    idx = -1

    for pv in possible_values:
        if not val(map(onp_expr, pv)):
            tab.append('F')
        else:
            tab.append('T')
        idx += 1

        if idx >= 1:
            if tab[idx-1] != tab[idx]:
                return False
    return 'T' if tab[n] == 'T' else 'F'

def alg(expr: str) -> str:
    st = []

    for e in expr:
        if e in string.ascii_lowercase + 'TF':
            st.append(e)

        elif e in '>|&/^':
            second_operand = st.pop()
            first_operand = st.pop()
            st.append("("+first_operand+e+second_operand+")" if e in "^|&/" else first_operand+e+second_operand)
        elif e == '~':
            if len(st) > 0:
                first_operand = st.pop()
                st.append('~' + first_operand)

    return  bracket(st.pop())


# Funkcja sprawdza czy dwa wyrażenia logiczne są sobie równe
# Funkcjonalność tą otrzymujemy dzięki poniższym krokom:
# 1) Znajdujemy postać ONP obu wyrażeń
# 2) Znajdujemy liczbę zmiennych w wyrażeniu drugim -> potrzebny, aby potem sprawdzać wartościowanie odpowiedniej
#    liczby zmiennych w drugim wyrażnieu (pv[:p])
# 3) Generujemy wszytskie ciągi zer i jedynek o długości równej liczbie zmiennych w pierwszym wyrażeniu
# 4) Iterujemy przez wyznaczone ciągi i sprawdzamy za pomocą wcześniej opisanej funkcji "val" czy oba wyrażenia są
#    równe dla danych ciagów zer i jednynek
# 5) Jeśli dla wszytskich ciągów wartośći obu wyrażeń są identyczne to zwracamy True w przeciwnym razie False

def equivalence(expr1: str, expr2: str) -> bool:

    onp_expr1 = onp(expr1)
    onp_expr2 = onp(expr2)

    idx = len(find_variable_in_expr(onp_expr2))

    possible_variables = gen(len(find_variable_in_expr(onp_expr1)))

    for pv in possible_variables:


        if val(map(onp_expr1, pv)) != val(map(onp_expr2, pv[:idx])):
            return False
    return True

# Funkcja napis złożony z wszytskich zmienncych występujących występujących w wyrażeniu wejściowym
def find_all_variables(expr: str) -> str:
    s = ''
    for e in expr:
        if e in string.ascii_lowercase and e not in 'ft':
            s += e
    return s


# Główna funkcja reukująca wyrażenie logiczne w następujących krokach:
# 1) Usuwamy spacje z wyrażenia wejściowego
# 2) Wyznaczamy zbiór zmiennych jak wszytskie wystąpienia zmiennych w napisie wejściowym oraz zmienne 'T' oraz 'F'
# 3) Wyznaczamy zbiór operatorów jak wszystkie operatory poza negacją przemnożone przez liczbę liczbę zmiennych
#    występującą w wyrażniu wejściowym pomniejszoną o jeden oraz operator negacji przemnożony przez liczbę zmienych z
#    wyrażenia wejściowego
# 4) Następnie sprawdzamy czy wyrażenie jest poprawne za pomocą funkcji check jeśli nie to zwracamy napis 'ERROR'
# 5) Jesli funkcja jest tautologią to zwracamy odpowiednio 'T' albo 'F'
# 6) Jeśli nie zaszedł żaden z dwóch powyższych warunków to w pętli generujemy wszystkie poprawne kombinacje o długośći
#    od 1 do długość wyrażenia wyjściowego pomniejszona o jeden i sprawdzamy czy tak otrzymane wyrażenie jest równowążne
#    naszemu wyrażeniu wyjściowemu.Jeśli tak to zwracamy je jako najkrótsza postać danego wyrażenia, jeśli nie udało się
#    znaleźć krótszej wersji to zwracamy wyrażenie wejściowe.


def reduce_expression(expr: str):

    expr1 = remove_spaces(expr)

    n = len(find_all_variables(expr1))
    variables =  find_all_variables(expr1) + 'TF'
    operands = "|/^&>"*(n-1) + '~'* (n//2)

    if not check(expr1):
        return 'ERROR'

    if t := tautology(expr1):
        return t

    for i in range(1, len(expr1)):
        for tmp_expr in var(variables+operands,i):

            if equivalence(expr1, tmp_expr):
                return tmp_expr
    return expr


def main() -> None:
    while True:
        expression = input()
        print(reduce_expression(expression))

if __name__ == '__main__':
    main()
