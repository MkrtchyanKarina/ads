from lab1.src.utils import File


def insertion_sort(array_len: int, not_sorted_array: list[int]) -> list[int]:
    array = not_sorted_array.copy()
    for i in range(1, array_len):
        for j in range(i-1, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i, j = j, i
    return array


def limits(array_len: int, array: list[int]) -> bool:
    if 1 <= array_len <= 10**3 and all(abs(el) <= 10**9 for el in array):
        return True
    else:
        return False


def addition_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))
    if limits(array_len, array):
        res = ' '.join(map(str, insertion_sort(array_len, array)))
        f.write(res)


if __name__ == "__main__":
    addition_txt()