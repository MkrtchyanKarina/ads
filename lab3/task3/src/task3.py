from lab3.src.utils import File


def scarecrow_sort(n: int, k: int, array: list) -> str:
    for i in range(k):
        for j in range(i+k, n, k):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    if all(array[i] <= array[i+1] for i in range(n-1)):
        return "ДА"
    else:
        return "НЕТ"


def limits(n: int, k: int, array: list[int]) -> bool:
    if 1 <= k < n <= 10**5 and all(abs(x) <= 10**9 for x in array):
        return True
    else:
        return False


def scarecrow_sort_txt():
    f = File(__file__)
    data = f.read()
    n, k = list(map(int, data[0].split(" ")))
    array = list(map(int, data[1].split(" ")))
    if limits(n, k, array):
        f.write(scarecrow_sort(n, k, array))


if __name__ == "__main__":
    scarecrow_sort_txt()