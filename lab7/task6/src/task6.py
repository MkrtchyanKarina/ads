import typing as tp
from lab6.src.utils import File
import math


def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x


def is_fib(n: int) -> str:
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return "Yes"
    else:
        return "No"


def limits(length: int, numbers: tp.List[int]) -> bool:
    if 1 <= length == len(numbers) <= 10 ** 6 and all(1 <= x <= 10 ** 5000 - 1 for x in numbers):
        return True
    else:
        return False


def is_fib_array_txt():
    f = File(__file__)
    arguments = f.read()
    length = int(arguments[0])
    numbers = [int(arguments[i]) for i in range(1, length + 1)]
    if limits(length, numbers):
        answer = "\n".join(is_fib(n) for n in numbers)
        f.write(answer)


if __name__ == "__main__":
    is_fib_array_txt()
