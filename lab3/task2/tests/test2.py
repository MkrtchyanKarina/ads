import unittest
import psutil
import time
from lab3.src.utils import table
from lab3.task2.src.task2 import worst_case
from colorama import Style

expected_time = 2
expected_memory = 256


class ScarecrowSortTest(unittest.TestCase):
    def test_worst_case0(self):
        # given
        n = 1
        expected_result = [1]

        # when
        t_start = time.perf_counter()
        result = worst_case(n)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result))])


    def test_worst_case1(self):
        # given
        n = 3
        expected_result = [1, 3, 2]

        # when
        t_start = time.perf_counter()
        result = worst_case(n)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result))])


    def test_worst_case2(self):
        # given
        n = 10
        expected_result = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        t_start = time.perf_counter()
        result = worst_case(n)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result))])

    def test_worst_case3(self):
        # given
        n = 10**6

        # when
        t_start = time.perf_counter()
        result = worst_case(n)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", n, t_end, memory,f'{" ".join(map(str, result[:10]))}...'])
        print()
        print(Style.BRIGHT + 'Task #2 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()