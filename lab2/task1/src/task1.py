from lab2.src.utils import File
import typing as tp


def merge_sort(array_len: int, array: tp.List[int]):
    middle = array_len // 2
    list_a, list_b = array[:middle], array[middle:]
    len_a, len_b = middle, array_len - middle
    if len_a > 1:
        list_a = merge_sort(len_a, list_a)
    if len_b > 1:
        list_b = merge_sort(len_b, list_b)
    return merge(len_a, len_b, list_a, list_b)


def merge(len_a: int, len_b: int, array_a: tp.List[int], array_b: tp.List[int]) -> tp.List[int]:
    len_c = len_a + len_b
    array_c = [0] * len_c
    index_a, index_b = 0, 0
    for index_c in range(len_c):
        if index_b >= len_b:
            array_c[index_c] = array_a[index_a]
            index_a += 1
        elif index_a >= len_a:
            array_c[index_c] = array_b[index_b]
            index_b += 1
        else:
            if array_a[index_a] <= array_b[index_b]:
                array_c[index_c] = array_a[index_a]
                index_a += 1
            else:
                array_c[index_c] = array_b[index_b]
                index_b += 1
    return array_c


def limits(n: int, m: list[int]) -> bool:
    if 1 <= n <= 2*10**4 and len(m) == n and all(abs(x) <= 10**9 for x in m):
        return True
    else:
        return False


def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        res = " ".join(map(str, merge_sort(array_len, array)))
        f.write(res)


if __name__ == "__main__":
    quick_sort_txt()
