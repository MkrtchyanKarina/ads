from lab1.src.utils import File


def insertion_sort(array_len, array):
    indexes = [1]
    for i in range(1, array_len):
        for j in range(i, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i, j = j, i
        indexes.append(i+1)
    return indexes, array


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
        res = insertion_sort(array_len, array)
        res1, res2 = ' '.join(map(str, res[0])), ' '.join(map(str, res[1]))
        f.write(res1 + "\n" + res2)


if __name__ == "__main__":
    addition_txt()