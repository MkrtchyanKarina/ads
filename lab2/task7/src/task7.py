from utils import File
import typing as tp


def line_find_max_subarray(array_len: int, array: tp.List[int]) -> tp.Tuple[int, int, int]:
    max_sum = 0
    start_index = 0
    end_index = 0
    sums = 0
    for i in range(array_len):
        if sums == 0:
            start_index = i
        sums += array[i]
        if max_sum < sums:
            max_sum = sums
            end_index = i
        if sums < 0:
            sums = 0
    if start_index <= end_index:
        return start_index, end_index, max_sum
    else:
        return start_index, end_index, 0


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
        res = line_find_max_subarray(array_len, array)
        f.write(" ".join(map(str, res)))



if __name__ == "__main__":
    quick_sort_txt()