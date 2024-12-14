import re
from lab3.src.utils import *


def h_index(citations: list[int]) -> int:
    res = 0
    citations = sorted(citations)[::-1]
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res += 1
    return res


def limits(citations: list[int]) -> bool:
    n = len(citations)
    if 1 <= n <= 5000 and all(0 <= i <= 1000 for i in citations):
        return True
    else:
        return False


def h_index_txt():
    f = File(__file__)
    args = list(map(int, re.split('[, ]', f.read()[0])))
    if limits(args):
        result = str(h_index(args))
        f.write(result)

if __name__ == "__main__":
    h_index_txt()