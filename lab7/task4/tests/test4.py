import time
import unittest
import psutil
from lab7.task4.src.task4 import longest_common_sub
from utils import table
from colorama import Style
from random import randint, shuffle

expected_time = 1
expected_memory = 128


class LongestCommonSubTest(unittest.TestCase):
    def test_longest_common_sub_0(self):
        # given
        n = 3
        arr_a = [2, 7, 5]
        m = 2
        arr_b = [2, 5]
        expected_result = 2

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a))}\n{m}\n{' '.join(map(str, arr_b))}'
        table.add_row(["Значения из примера", arguments, t_end, memory, result])


    def test_longest_common_sub_1(self):
        # given
        n = 1
        arr_a = [7]
        m = 4
        arr_b = [1, 2, 3, 4]
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a))}\n{m}\n{' '.join(map(str, arr_b))}'
        table.add_row(["Значения из примера", arguments, t_end, memory, result])

    def test_longest_common_sub_2(self):
        # given
        n = 4
        arr_a = [2, 7, 8, 3]
        m = 4
        arr_b = [5, 2, 8, 7]
        expected_result = 2

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a))}\n{m}\n{' '.join(map(str, arr_b))}'
        table.add_row(["Значения из примера", arguments, t_end, memory, result])

    def test_longest_common_sub_3(self):
        # given
        n = 100
        arr_a = [randint(-10**9, 10**9) for _ in range(n)]
        m = 100
        arr_b = arr_a.copy()
        shuffle(arr_b)

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a[:4]))}\n{m}\n{' '.join(map(str, arr_b[:4]))}'
        table.add_row(["Максимальные значения", arguments, t_end, memory, result])


        print()
        print(Style.BRIGHT + 'Lab #7 |Task #4 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()