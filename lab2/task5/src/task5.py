import typing as tp
from lab2.src.utils import File


def frequent(high: int, array: tp.List[int]) -> int:
    dictionary = {}
    res = 1
    for index in range(high):
        elem = array[index]
        if elem in dictionary:
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1
        if dictionary[elem] > high / 2:
            return 1
        else:
            res = 1
    if res:
        return 0


def limits(n: int, m: list[int]) -> bool:
    if 1 <= n <= 10**5 and len(m) == n and all(abs(x) <= 10**9 for x in m):
        return True
    else:
        return False


def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        res = frequent(array_len, array)
        f.write(str(res))


if __name__ == "__main__":
    quick_sort_txt()
