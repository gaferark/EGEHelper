from math import factorial as fact
from EGEHelper import Rationale as Rt


def r_coef(n):
    result = [Rt(i, fact(i + 1)) for i in range(1, n)]
    for m in range(1, n):
        result[m - 1] -= sum(result[k - 1] / fact(m + 1 - k) for k in range(1, m))
    return [Rt(1, 1)] + result

print(~ 0)