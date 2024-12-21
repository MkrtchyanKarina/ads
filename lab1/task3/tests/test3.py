from lab1.task3.src.task3 import insertion_sort
import unittest
import psutil
import time
from random import randint
from utils import table
from colorama import Style


expected_time = 2
expected_memory = 256


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort_0(self):
        # given
        array_len = 1
        array = [0]
        expected_result = sorted(array)[::-1]

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,  ' '.join(map(str, result))])

    def test_insertion_sort_1(self):
        # given
        array_len = 6
        array = [31, 41, 59, 26, 41, 58]
        expected_result = sorted(array)[::-1]

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,  ' '.join(map(str, result))])

    def test_insertion_sort_2(self):
        # given
        array_len = 100
        array = [randint(-10**9, 10**9) for _ in range(array_len)]
        expected_result = sorted(array)[::-1]

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{' '.join(map(str, array[:4]))}', t_end, memory,  ' '.join(map(str, result[:4]))])


    def test_insertion_sort_3(self):
        # given
        array_len = 1000
        array = [randint(-10**9, 10**9) for _ in range(array_len)]
        expected_result = sorted(array)[::-1]

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{array_len}\n{' '.join(map(str, array[:4]))}', t_end, memory,  ' '.join(map(str, result[:4]))])

        print()
        print(Style.BRIGHT + 'Lab #1 | Task #3 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
