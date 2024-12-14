import unittest
import psutil
import time
from random import randint
from lab2.src.utils import table
from lab2.task3.src.task3 import PermutationsCount
from colorama import Style

expected_time = 2
expected_memory = 256


def bubble_sort(array_len, array):
    count = 0
    sorting_array = array.copy()
    for i in range(array_len):
        for j in range(0, array_len - i - 1):

            if sorting_array[j] > sorting_array[j + 1]:
                sorting_array[j], sorting_array[j + 1] = sorting_array[j + 1], sorting_array[j]
                count += 1
    return count


class PermutationsCountTest(unittest.TestCase):

    def test_permutations_count_0(self):
        # given
        array_len = 1
        array = [0]
        expected_result = bubble_sort(array_len, array)

        # when
        t_start = time.perf_counter()
        result = PermutationsCount().return_count(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{" ".join(map(str, array))}', t_end, memory, result])


    def test_permutations_count_1(self):
        # given
        array_len = 1_000
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]
        expected_result = bubble_sort(array_len, array)

        # when
        t_start = time.perf_counter()
        result = PermutationsCount().return_count(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])

    def test_permutations_count_2(self):
        # given
        array_len = 10_000
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = PermutationsCount().return_count(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])

    def test_permutations_count_3(self):
        # given
        array_len = 100_000
        array = [randint(-10 ** 9, 10 ** 9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = PermutationsCount().return_count(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{" ".join(map(str, array[:3]))}', t_end, memory, result])
        print()
        print(Style.BRIGHT + 'Task #3 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()

