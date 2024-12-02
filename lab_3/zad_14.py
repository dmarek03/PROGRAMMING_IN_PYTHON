#Napisać generator generujący k elementowe wariacje bez powtórzeń ze zbioru liter w napisie

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


def var(s, k):
    for c in comb(s,k):
        for p in perm(c):
            yield p
#
# cnt = 0
# for v in var("aa||c", 3):
#     cnt += 1
#     print(v)
# print(cnt)
x = "(a^b)>d"
cnt1 = 0
for c in var("abd~~~^^//>>||&&TF()", 9):
    cnt1 +=1
    if c == "(a^b)>d":
        print(c)
        break

print(cnt1)

