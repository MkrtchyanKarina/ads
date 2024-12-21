from utils import File


def longest_common_sub(n, arr_a, m, arr_b):
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            if arr_a[i - 1] == arr_b[j - 1]:
                matrix[i][j] = max(matrix[i][j], matrix[i - 1][j - 1] + 1)
    return matrix[n][m]


def limits(n: int, arr_a: list[int], m: int, arr_b: list[int]) -> bool:
    if (1 <= n <= 100) and (len(arr_a) == n) and all(abs(x) <= 10**9 for x in arr_a):
        if (1 <= m <= 100) and (len(arr_b) == n) and all(abs(x) <= 10 ** 9 for x in arr_b):
            return True
    return False


def longest_common_sub_txt():
    f = File(__file__)
    arguments = f.read()

    n = int(arguments[0])
    arr_a = list(map(int, arguments[1].split(" ")))

    m = int(arguments[2])
    arr_b = list(map(int, arguments[3].split(" ")))

    answer = longest_common_sub(n, arr_a, m, arr_b)
    f.write(str(answer))


if __name__ == "__main__":
    longest_common_sub_txt()
