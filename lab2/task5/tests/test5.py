import unittest
import psutil
import time
from random import randint, shuffle
from utils import table
from lab2.task5.src.task5 import frequent
from colorama import Style

expected_time = 2
expected_memory = 256


class FrequentTest(unittest.TestCase):

    def test_frequent_0(self):
        # given
        array_len = 1
        array = [0]
        expected_result = 1

        # when
        t_start = time.perf_counter()
        result = frequent(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{array_len}\n{" ".join(map(str, array))}', t_end, memory, result])


    def test_frequent_1(self):
        # given
        array_len = 5
        array = [2, 3, 9, 2, 2]
        expected_result = 1

        # when
        t_start = time.perf_counter()
        result = frequent(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array))}', t_end, memory, result])

    def test_frequent_2(self):
        # given
        array_len = 4
        array = [1, 2, 3, 4]
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = frequent(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{" ".join(map(str, array))}', t_end, memory, result])

    def test_merge_sort_3(self):
        # given
        array_len = 10**5
        elem = randint(-10**9, 10**9)
        array = ([randint(-10**9, 10**9) for _ in range(array_len//2-1)] +
                 [elem for _ in range(array_len//2+1)])
        shuffle(array)
        expected_result = 1

        # when
        t_start = time.perf_counter()
        result = frequent(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{array_len}\n{" ".join(map(str, array[-4:]))}', t_end, memory, result])

    def test_merge_sort_4(self):
        # given
        array_len = 10**5
        array = [randint(-10**9, 10**9) for _ in range(array_len)]
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = frequent(array_len, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{array_len}\n{" ".join(map(str, array[-4:]))}', t_end, memory, result])

        print()
        print(Style.BRIGHT + 'Lab #2 | Task #5 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
