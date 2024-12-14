import typing as tp
from lab5.src.utils import File


def is_heap(array_len: int, array: tp.List[int]) -> str:
    for index in range(array_len // 2):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if array[index] > array[left_index]:
            return "NO"
        if right_index < len(array) and array[index] > array[right_index]:
            return "NO"
    return "YES"


def limits(n: int, array: tp.List[int]) -> bool:
    if (1 <= n <= 10**6) and (len(array) == n) and all(abs(x) <= 2*10**9 for x in array):
        return True
    else:
        return False


def is_heap_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        answer = is_heap(array_len, array)
        f.write(answer)


if __name__ == "__main__":
    is_heap_txt()