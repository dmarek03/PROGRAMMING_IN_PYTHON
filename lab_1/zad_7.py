"""
7. Proszę napisać funkcję val(expr) obliczająca wartość wyrażenia logicznego expr.
Na przykład:
val(‘10>’) -> 0
val(‘110>&’) -> 1
"""


def val(expr):
    st = []
    for e in expr:

        if e in '01TF':
            if e == "T":
                st.append(1)

            elif e == "F":
                st.append(0)
            else:
                st.append(int(e))
            #print(f'{st=}')

        elif e == '|':
            second_var = st.pop()
            first_var = st.pop()
            # print(f'{first_var=}')
            # print(f'{second_var=}')
            st.append(first_var or second_var)
            #print(f'After alternative: {st=}')

        elif e == '&':
            second_var = st.pop()
            first_var = st.pop()
            # print(f'{first_var=}')
            # print(f'{second_var=}')
            st.append(first_var and second_var)
           #print(f'After conjunction  : {st=}')

        elif e == '>':
            second_var = st.pop()
            first_var = st.pop()
            # print(f'{first_var=}')
            # print(f'{second_var=}')

            st.append((1-first_var) or second_var)
            #print(f'After implication: {st=}')

        elif e == "^":
            second_var = st.pop()
            first_var = st.pop()
            st.append(((first_var or second_var) and (1-(first_var and second_var))))

        elif e == "/":
            second_var = st.pop()
            first_var = st.pop()
            st.append(1-(first_var and second_var))

        elif e == '~':
            #print("negation")
            first_var = st.pop()
            st.append(1-first_var)


        else:
            break
    return st.pop()


if __name__ == '__main__':
    # print(val("10>"))
    #print(val("10^"))
    #print(val("0~0~|~"))
    print(val("11~|11~|&F|"))
