from lab7.src.utils import File


def longest_sub(array_len: int, array: list[int]) -> tuple[int, list[int]]:
    inf = 10**10
    subsequence = [inf] * (array_len + 1)
    subsequence[0] = -inf
    for i in range(array_len):
        left = 0
        right = array_len
        while right - left > 1:
            middle = (left + right) // 2
            if subsequence[middle] >= array[i]:
                right = middle
            else:
                left = middle
        subsequence[right] = array[i]
    longest_subsequence = subsequence[1:subsequence.index(inf)]
    return len(longest_subsequence), longest_subsequence


def limits(array_len: int, array: list[int]) -> bool:
    if 1 <= array_len == len(array) <= 3*10**5 and all(abs(x) <= 10 ** 9 for x in array):
        return True
    else:
        return False


def longest_sub_txt() -> None:
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))
    if limits(array_len, array):
        result = longest_sub(array_len, array)
        answer = f'{result[0]}\n{' '.join(map(str, result[1]))}'
        f.write(answer)


if __name__ == "__main__":
    longest_sub_txt()
