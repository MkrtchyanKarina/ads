from lab0.src.utils import File


def last_digit(n: int) -> int:
    return fast_multiply([[0, 1], [1, 1]], n, m=10)[0][1]


def fast_multiply(x: list[list[int]], n: float, m: int):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        y = fast_multiply(x, n / 2, m)
        return matrix_multiply_2x2(y, y, m)
    else:
        y = fast_multiply(x, (n - 1) / 2, m)
        y2 = matrix_multiply_2x2(y, y, m)
        return matrix_multiply_2x2(y2, x, m)


def matrix_multiply_2x2(a: list[list[int]], b: list[list[int]], m: int):
    result_matrix = [[0, 0], [0, 0]]
    result_matrix[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
    result_matrix[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
    result_matrix[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
    result_matrix[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
    return result_matrix


def limits(number: int) -> bool:
    if 0 <= number <= 10**7:
        return True
    else:
        return False


def addition_sqrt_txt():
    f = File(__file__)
    arguments = f.read()
    number = int(arguments[0])
    if limits(number):
        res = str(last_digit(number))
        f.write(res)


if __name__ == "__main__":
    addition_sqrt_txt()
