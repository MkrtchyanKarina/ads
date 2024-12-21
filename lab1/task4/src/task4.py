from utils import File


def lineal_search(array: list[int], element: int) -> tuple[int, list[int]]:
    indexes = []
    for i in range(len(array)):
        if array[i] == element:
            indexes.append(i)
    count = len(indexes)
    if count == 0:
        return 0, [-1]
    else:
        return count, indexes


def limits(array: list[int], element: int) -> bool:
    if 1 <= len(array) <= 10**3 and all(abs(el) <= 10**3 for el in array+[element]):
        return True
    else:
        return False


def lineal_search_txt():
    f = File(__file__)
    arguments = f.read()
    array = list(map(int, arguments[0].split(" ")))
    element = int(arguments[1])
    if limits(array, element):
        res = ""
        count, indexes = lineal_search(array, element)
        if count == 0:
            res += "-1"
        elif count == 1:
            res += str(indexes[0])
        else:
            res += f"{count}\n{", ".join(map(str, indexes))}"
        f.write(res)


if __name__ == "__main__":
    lineal_search_txt()