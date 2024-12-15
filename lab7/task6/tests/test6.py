import time
import unittest
import psutil
from lab7.task6.src.task6 import longest_sub
from lab7.src.utils import table
from colorama import Style
from random import randint

expected_time = 2
expected_memory = 256



class LongestSubTest(unittest.TestCase):
    def test_longest_sub_0(self):
        # given
        array_len = 6
        array = [3, 29, 5, 5, 28, 6]
        expected_result = (3, [3, 5, 6])

        # when
        t_start = time.perf_counter()
        result = longest_sub(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,f'{result[0]}\n{' '.join(map(str, result[1]))}'])


    def test_longest_sub_1(self):
        # given
        array_len = 10
        array = [-5, 3, 2, 3, -6, 2, 8, 1, 10, 4]
        expected_result = (5, [-6, 1, 3, 4, 10])

        # when
        t_start = time.perf_counter()
        result = longest_sub(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{' '.join(map(str, array))}', t_end, memory,f'{result[0]}\n{' '.join(map(str, result[1]))}'])


    def test_longest_sub_2(self):
        # given
        array_len = 5_000
        array = [randint(-10**9, 10**9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = longest_sub(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{' '.join(map(str, array[:4]))}', t_end, memory,f'{result[0]}\n{' '.join(map(str, result[1][:4]))}'])


    def test_longest_sub_3(self):
        # given
        array_len = 300_000
        array = [randint(-10**9, 10**9) for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = longest_sub(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{array_len}\n{' '.join(map(str, array[:4]))}', t_end, memory,f'{result[0]}\n{' '.join(map(str, result[1][:4]))}'])


        print()
        print(Style.BRIGHT + 'Lab #7 | Task #6 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()