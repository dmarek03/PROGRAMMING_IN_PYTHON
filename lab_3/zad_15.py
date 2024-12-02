# generator podzbiorów


def subset(s):
    if len(s) == 0:
        yield ""
    else:
        for sb in subset(s[1:]):
            yield sb
            yield s[0] + sb

for sb in subset("abcde"):
    print(sb)