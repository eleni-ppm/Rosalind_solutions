
def iprb(k, m, n):
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    j = 4 * (k + m + n) * (k + m + n - 1)
    rst = 1 - float(i) / j
    return rst

k = 2
m = 2
n = 2
print(iprb(k, m, n))