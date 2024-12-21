from lab1.task2.src.task2 import insertion_sort
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
        expected_result = ([1], [0])

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        res1, res2 = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,
                       f"{' '.join(map(str, res1))}\n{' '.join(map(str, res2))}"])

    def test_insertion_sort_1(self):
        # given
        array_len = 10
        array = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_result = ([1, 2, 2, 2, 3, 5, 5, 6, 9, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        res1, res2 = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,
                       f"{' '.join(map(str, res1))}\n{' '.join(map(str, res2))}"])

    def test_insertion_sort_2(self):
        # given
        array_len = 1000
        array = [randint(-10**9, 10**9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = insertion_sort(array_len, array)
        res1, res2 = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{' '.join(map(str, array[:4]))}', t_end, memory,
                       f"{' '.join(map(str, res1[:4]))}\n{' '.join(map(str, res2[:4]))}"])

        print()
        print(Style.BRIGHT + 'Lab #1 | Task #2 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()



if __name__ == "__main__":
    unittest.main()
