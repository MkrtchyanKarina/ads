from lab6.src.utils import File


def longest_common_sub(len1, array1, len2, array2):
    matrix = [[0] * (len2 + 1) for _ in range(len1+1)]
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            if array1[i-1] == array2[j-1]:
                matrix[i][j] = max(matrix[i][j], matrix[i - 1][j - 1] + 1)
        print(matrix)
    return matrix[len1][len2]

print(longest_common_sub(3, [2, 7, 5], 2, [2, 5]))

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
