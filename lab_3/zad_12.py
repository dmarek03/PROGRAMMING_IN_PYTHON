#  generator generujący kombinacje k elementowe ze zbioru liter w napisie

def comb(text, k):
    if k == 1:
        for t in text:
            yield [t]

    elif len(text) == k:
        yield text
    else:

        for c in comb(text[1:], k-1):
            yield [text[0]] + c

        for c in comb(text[1:], k):
            yield c

for c in comb([1, 2, 3, 4, 5 ], 3):
    print(c)


x = [c for c in  comb([1, 2, 3, 4, 5 ], 3)]
print(x)
