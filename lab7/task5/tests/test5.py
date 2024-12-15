import time
import unittest
import psutil
from lab7.task5.src.task5 import longest_common_sub
from lab7.src.utils import table
from colorama import Style
from random import randint, shuffle

expected_time = 1
expected_memory = 64



class LongestCommonSubTest(unittest.TestCase):
    def test_longest_common_sub_0(self):
        # given
        n = 3
        arr_a = [1, 2, 3]
        m = 3
        arr_b = [2, 1, 3]
        l = 3
        arr_c = [1, 3, 5]
        expected_result = 2

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b, l, arr_c)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a))}\n{m}\n{' '.join(map(str, arr_b))}\n{l}\n{' '.join(map(str, arr_c))}'
        table.add_row(["Значения из примера", arguments, t_end, memory, result])


    def test_longest_common_sub_1(self):
        # given
        n = 5
        arr_a = [8, 3, 2, 1, 7]
        m = 7
        arr_b = [8, 2, 1, 3, 8, 10, 7]
        l = 6
        arr_c = [6, 8, 3, 1, 4, 7]
        expected_result = 3

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b, l, arr_c)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a))}\n{m}\n{' '.join(map(str, arr_b))}\n{l}\n{' '.join(map(str, arr_c))}'
        table.add_row(["Значения из примера", arguments, t_end, memory, result])

    def test_longest_common_sub_2(self):
        # given
        n = 100
        arr_a = [randint(-10**9, 10**9) for _ in range(n)]
        m = 100
        arr_b = arr_a.copy()
        shuffle(arr_b)
        l = 100
        arr_c = arr_a.copy()
        shuffle(arr_c)

        # when
        t_start = time.perf_counter()
        result = longest_common_sub(n, arr_a, m, arr_b, l, arr_c)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        arguments = f'{n}\n{' '.join(map(str, arr_a[:4]))}\n{m}\n{' '.join(map(str, arr_b[:4]))}\n{l}\n{' '.join(map(str, arr_c[:4]))}'
        table.add_row(["Максимальные значения", arguments, t_end, memory, result])


        print()
        print(Style.BRIGHT + 'Task #5 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()