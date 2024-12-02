# Wyrażenie generujące

n = 24
g = (p for p in range(1, n) if n % p == 0)
next(g)