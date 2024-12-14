from lab6.src.utils import File


def longest_common_sub(n, arr_a, m, arr_b, l, arr_c):
    matrix = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
                if arr_a[i - 1] == arr_b[j - 1] == arr_c[k - 1]:
                    matrix[i][j][k] = max(matrix[i][j][k], matrix[i - 1][j - 1][k - 1] + 1)

    return matrix[n][m][l]


print(longest_common_sub(3, [1, 2, 3], 3, [2, 1, 3], 3, [1, 3, 5]))

# def elections_txt():
#     f = File(__file__)
#     arguments = f.read()
#     states_result = arguments
#     answer = elections(states_result)
#     f.write('\n'.join(answer))
#
#
# if __name__ == "__main__":
#     elections_txt()
