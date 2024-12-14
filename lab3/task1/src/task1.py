from random import randint
from lab3.src.utils import File


def quick_sort(l: list[int]) -> list[int]:
    m = l.copy()
    if len(m) > 1:
        pivot = m[randint(0, len(m) - 1)]
        start = [i for i in m if i < pivot]
        equal = [i for i in m if i == pivot]
        end = [i for i in m if i > pivot]
        m = quick_sort(start) + equal + quick_sort(end)
    return m


def limits(n: int, m: list[int]) -> bool:
    if 1 <= n <= 10**4 and len(m) == n and all(abs(x) <= 10**9 for x in m):
        return True
    else:
        return False


def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    n = int(arguments[0])
    m = list(map(int, arguments[1].split(" ")))

    if limits(n, m):
        res = " ".join(map(str, quick_sort(m)))
        f.write(res)


if __name__ == "__main__":
    quick_sort_txt()