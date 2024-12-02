# Generator generujący permutacje liter w napisie


def perm(s):
    if len(s) == 1:
        yield s

    else:
        for p in perm(s[1:]):
            for i in range(len(s)):
                yield p[:i] + s[0] + p[i:]


for p in perm("abc~|/^&"):
    #if p in ["a|b|c", "a|c|b", "b|a|c", "b|c|a", "c|a|b", "c|b|a"]:
        print(p)