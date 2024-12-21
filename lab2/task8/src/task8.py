from math import log2, ceil
from utils import File


def karatsuba_polynomial_multiply(A, B):
    return reformat(multiply(power_of_two(A), power_of_two(B)))


def multiply(poly1, poly2):

    n = len(poly1)
    if n == 1:
        return [poly1[0] * poly2[0]]

    mid = n // 2
    a = poly1[:mid]
    b = poly1[mid:]
    c = poly2[:mid]
    d = poly2[mid:]

    ac = multiply(a, c)
    bd = multiply(b, d)
    third_product = multiply([a[i] + b[i] for i in range(mid)], [c[i] + d[i] for i in range(mid)])

    middle = [third_product[i] - ac[i] - bd[i] for i in range(len(third_product))]
    result = []

    n = []
    i = 3
    while i <= len(ac):
        n.append(i)
        i = 2*i + 1
    if len(ac) in n:
        result += union(ac, middle, bd)
        return result
    else:
        return ac + middle + bd


def union(a, b, c):
    n = len(a) // 2
    return a[:-n] + [a[-n + i] + b[i] for i in range(n)] + b[n:-n] + [b[-n + i] + c[i] for i in range(n)] + c[n:]


def power_of_two(m):
    n = len(m)
    return [0] * (2 ** ceil(log2(n)) - n) + m


def reformat(x):
    for i in range(len(x)):
        if x[i] != 0:
            return x[i:]


def limits(n: int, A: list[int], B: list[int]) -> bool:
    if len(A) == len(B) == n:
        return True
    else:
        return False


def karatsuba_polynomial_multiply_txt():
    f = File(__file__)
    arguments = f.read()
    n = int(arguments[0])
    A = list(map(int, arguments[1].split(" ")))
    B = list(map(int, arguments[2].split(" ")))

    if limits(n, A, B):
        res = karatsuba_polynomial_multiply(A, B)
        f.write(' '.join(map(str, res)))


if __name__ == "__main__":
    karatsuba_polynomial_multiply_txt()
