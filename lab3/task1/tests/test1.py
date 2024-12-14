import unittest
from random import randint
import psutil
import time
from lab3.src.utils import table
from lab3.task1.src.task1 import quick_sort
from colorama import Style

expected_time = 2
expected_memory = 256


class QuickSortTest(unittest.TestCase):
    def test_quick_sort0(self):
        # given
        n = 1
        m = [randint(-10, 10) for i in range(n)]
        expected_result = sorted(m)

        # when
        t_start = time.perf_counter()
        result = quick_sort(m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, m))}', t_end, memory, " ".join(map(str, result))])


    def test_quick_sort1(self):
        # given
        n = 5
        m = [2, 3, 9, 2, 2]
        expected_result = sorted(m)

        # when
        t_start = time.perf_counter()
        result = quick_sort(m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, m))}', t_end, memory, " ".join(map(str, result))])

    def test_quick_sort2(self):
        # given
        n = 10
        m = [randint(-100, 100) for i in range(n)]
        expected_result = sorted(m)

        # when
        t_start = time.perf_counter()
        result = quick_sort(m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, m))}', t_end, memory, " ".join(map(str, result))])

    def test_quick_sort3(self):
        # given
        n = 10**4
        m = [randint(-10**9, 10**9) for i in range(n)]
        expected_result = sorted(m)

        # when
        t_start = time.perf_counter()
        result = quick_sort(m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{n}\n{" ".join(map(str, m[:3]))}...', t_end, memory, f'{" ".join(map(str, result[:3]))}...'])
        print()
        print(Style.BRIGHT + 'Task #1 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()