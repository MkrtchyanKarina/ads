from lab0.src.utils import File


def fib_number(number: int) -> int:
    return fast_multiply([[0, 1], [1, 1]], number)[0][1]


def fast_multiply(coefficient, number):
    if number == 0:
        return [[1, 0], [0, 1]]
    elif number % 2 == 0:
        y = fast_multiply(coefficient, number / 2)
        return matrix_multiply_2x2(y, y)
    else:
        y = fast_multiply(coefficient, (number - 1) / 2)
        y2 = matrix_multiply_2x2(y, y)
        return matrix_multiply_2x2(y2, coefficient)


def matrix_multiply_2x2(first_matrix: list[list[int]], second_matrix):
    result_matrix = [[0, 0], [0, 0]]
    result_matrix[0][0] = (first_matrix[0][0] * second_matrix[0][0] + first_matrix[0][1] * second_matrix[1][0])
    result_matrix[1][0] = (first_matrix[1][0] * second_matrix[0][0] + first_matrix[1][1] * second_matrix[1][0])
    result_matrix[0][1] = (first_matrix[0][0] * second_matrix[0][1] + first_matrix[0][1] * second_matrix[1][1])
    result_matrix[1][1] = (first_matrix[1][0] * second_matrix[0][1] + first_matrix[1][1] * second_matrix[1][1])
    return result_matrix


def limits(number: int) -> bool:
    if 0 <= number <= 2*10**4:
        return True
    else:
        return False


def addition_sqrt_txt():
    f = File(__file__)
    arguments = f.read()
    number = int(arguments[0])
    if limits(number):
        res = str(fib_number(number))
        f.write(res)


if __name__ == "__main__":
    addition_sqrt_txt()

