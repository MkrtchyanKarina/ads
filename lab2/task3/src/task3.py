import typing as tp
from utils import File


class PermutationsCount:
    def __init__(self) -> None:
        self.permutations_count = 0

    def merge_sort(self, array_len: int, array: tp.List[int]) -> tp.List[int]:
        middle = array_len // 2
        list_a, list_b = array[:middle], array[middle:]
        len_a, len_b = middle, array_len - middle
        if len_a > 1:
            list_a = self.merge_sort(len_a, list_a)
        if len_b > 1:
            list_b = self.merge_sort(len_b, list_b)
        return self.merge(len_a, len_b, list_a, list_b)

    def merge(self, len_a: int, len_b: int, array_a: tp.List[int], array_b: tp.List[int]) -> tp.List[int]:

        len_c = len_a + len_b
        array_c = [0] * len_c
        count = 0
        index_a, index_b = 0, 0
        for index_c in range(len_c):
            if index_b >= len_b:
                array_c[index_c] = array_a[index_a]
                step = abs(index_c - index_a)
                index_a += 1
            elif index_a >= len_a:
                array_c[index_c] = array_b[index_b]
                step = abs(index_c - len_a - index_b)
                index_b += 1
            else:
                if array_a[index_a] <= array_b[index_b]:
                    array_c[index_c] = array_a[index_a]
                    step = abs(index_c - index_a)
                    index_a += 1
                else:
                    array_c[index_c] = array_b[index_b]
                    step = abs(index_c - len_a - index_b)
                    index_b += 1
            count += step
        self.permutations_count += count // 2
        return array_c

    def return_count(self, array_len: int, array: tp.List[int]) -> int:
        self.merge_sort(array_len, array)
        return self.permutations_count


def limits(n: int, m: list[int]) -> bool:
    if 1 <= n <= 10**5 and len(m) == n and all(abs(x) <= 10**9 for x in m):
        return True
    else:
        return False


def return_count_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        ex = PermutationsCount()
        res = ex.return_count(array_len, array)
        f.write(str(res))


if __name__ == "__main__":
    return_count_txt()