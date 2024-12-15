from lab7.src.utils import File


def longest_common_sub(n: int, arr_a: list[int], m: int, arr_b: list[int], l: int, arr_c: list[int]) -> int:
    matrix = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
                if arr_a[i - 1] == arr_b[j - 1] == arr_c[k - 1]:
                    matrix[i][j][k] = max(matrix[i][j][k], matrix[i - 1][j - 1][k - 1] + 1)
    return matrix[n][m][l]


def limits(n: int, arr_a: list[int], m: int, arr_b: list[int], l: int, arr_c: list[int]) -> bool:
    if (1 <= n <= 100) and (len(arr_a) == n) and all(abs(x) <= 10**9 for x in arr_a):
        if (1 <= m <= 100) and (len(arr_b) == n) and all(abs(x) <= 10 ** 9 for x in arr_b):
            if (1 <= l <= 100) and (len(arr_c) == n) and all(abs(x) <= 10 ** 9 for x in arr_c):
                return True
    return False


def longest_common_sub_txt():
    f = File(__file__)
    arguments = f.read()

    n = int(arguments[0])
    arr_a = list(map(int, arguments[1].split(" ")))

    m = int(arguments[2])
    arr_b = list(map(int, arguments[3].split(" ")))

    l = int(arguments[4])
    arr_c = list(map(int, arguments[5].split(" ")))

    answer = longest_common_sub(n, arr_a, m, arr_b, l, arr_c)
    f.write(str(answer))


if __name__ == "__main__":
    longest_common_sub_txt()
