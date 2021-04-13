def gcd(n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    if n >= m:
        return gcd(n % m, m)
    if n <= m:
        return gcd(n, m % n)
