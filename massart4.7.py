import math


def rac_eq_2nd_deg(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return tuple()

    elif d == 0:
        r1 = ((-b + math.sqrt(d)) / (2 * a))
        return (r1,)
    else:
        r1 = ((-b + math.sqrt(d)) / (2 * a))
        r2 = ((-b - math.sqrt(d)) / (2 * a))
        return min(r1, r2), max(r1, r2)