import unittest
import psutil
import time
import random
from utils import table
from lab2.task8.src.task8 import karatsuba_polynomial_multiply
from colorama import Style

expected_time = 2
expected_memory = 256


def poly_multiply_slow(n, A, B):
    C = [0] * (2*n - 1)
    for i in range(n):
        for j in range(n):
            C[i+j] += A[i] * B[j]
    return C


class PolyMultiplyTest(unittest.TestCase):
    def test_multiply1(self):
        n = 1
        A = [4]
        B = [5]
        expected_result = [20]

        # when
        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(A, B)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, A[:3]))}\n{" ".join(map(str, B[:3]))}',
                       t_end, memory, " ".join(map(str, result[:3]))])

    def test_multiply2(self):
        n = 100
        A = [random.randint(-10 ** 3, 10 ** 3) for _ in range(n)]
        B = [random.randint(-10 ** 3, 10 ** 3) for _ in range(n)]
        expected_result = poly_multiply_slow(n, A, B)

        # when
        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(A, B)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, A[:3]))}\n{" ".join(map(str, B[:3]))}',
                       t_end, memory, " ".join(map(str, result[:3]))])

    def test_multiply3(self):
        n = 10**3
        A = [random.randint(-10 ** 5, 10 ** 5) for _ in range(n)]
        B = [random.randint(-10 ** 5, 10 ** 5) for _ in range(n)]
        expected_result = poly_multiply_slow(n, A, B)

        # when
        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(A, B)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, A[:3]))}\n{" ".join(map(str, B[:3]))}',
                       t_end, memory, " ".join(map(str, result[:3]))])

        print()
        print(Style.BRIGHT + 'Lab #2 | Task #8 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
