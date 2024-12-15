from lab2.task7.src.task7 import line_find_max_subarray
import unittest
import psutil
import time
from random import randint
from lab2.src.utils import table
from colorama import Style

expected_time = 2
expected_memory = 256


class MaxSubarrayTest(unittest.TestCase):
    def test_frequent_0(self):
        # given
        array_len = 1
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = line_find_max_subarray(array_len, array)
        expected_result = max(0, sum(array[result[0]:result[1] + 1]))
        result = result[2]
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])


    def test_frequent_1(self):
        # given
        array_len = 1_000
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = line_find_max_subarray(array_len, array)
        expected_result = max(0, sum(array[result[0]:result[1] + 1]))
        result = result[2]
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])

    def test_frequent_2(self):
        # given
        array_len = 10_000
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = line_find_max_subarray(array_len, array)

        expected_result = max(0, sum(array[result[0]:result[1] + 1]))
        result = result[2]
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])



    def test_frequent_3(self):
        # given
        array_len = 100_000
        array = [randint(-10 ** 9, 10 ** 9) for i in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = line_find_max_subarray(array_len, array)
        expected_result = max(0, sum(array[result[0]:result[1] + 1]))
        result = result[2]
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])

        print()
        print(Style.BRIGHT + 'Lab #2 | Task #7 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
