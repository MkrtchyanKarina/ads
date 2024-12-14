from lab3.src.utils import *
import typing as tp


def strings_sort(n: int, m: int, k: int, strings: tp.List[str]):
    strings = reformat(n, strings)
    for ind in range(m-1, m-k-1, -1):
        strings = radix_sort(ind, strings)
    return [s[0] for s in strings]


def radix_sort(k: int, strings: list[tp.List[str]]) -> list[int]:
    alf = {i:[] for i in range(97, 123)}
    for s in strings:
        alf[ord(s[1][k])] += [s]
    return sum(alf.values(), [])


def limits(n:int, m: int, k:int, strings: tp.List[str]):
    if (1 <= n <= 10**6) and (1 <= k <= m <= 10**6) and (n*m <= 5*10**7) and (len(strings) == n) and all(len(s) == m for s in strings):
        return True
    else:
        return False


def reformat(n, strings):
    strings_indexes = []
    for s in range(n):
        strings_indexes.append([s+1, strings[s]])
    return strings_indexes


def strings_sort_txt():
    f = File(__file__)
    arguments = f.read()
    n, m, k = list(map(int, arguments[0].split()))
    strings = []
    for s in range(n):
        strings.append(arguments[s+1])
    if limits(n, m, k, strings):
        res = ' '.join(map(str, strings_sort(n, m, k, strings)))
        f.write(res)

if __name__ == "__main__":
    strings_sort_txt()