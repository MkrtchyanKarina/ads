import unittest
import psutil
import time
from random import randint
from utils import table
from lab3.task5.src.task5 import h_index
from scholarmetrics import hindex
from colorama import Style

expected_time = 1
expected_memory = 64


class HIndexTest(unittest.TestCase):
    def test_str_sort0(self):
        # given
        citations = [randint(2, 19)]
        expected_result = hindex(citations)

        # when
        t_start = time.perf_counter()
        result = h_index(citations)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{' '.join(map(str, citations))}', t_end, memory, result])

    def test_str_sort1(self):
        # given
        citations = [1, 3, 1]
        expected_result = hindex(citations)

        # when
        t_start = time.perf_counter()
        result = h_index(citations)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{' '.join(map(str, citations))}', t_end, memory, result])

    def test_str_sort2(self):
        # given
        citations = [3, 0, 6, 1, 5]
        expected_result = hindex(citations)

        # when
        t_start = time.perf_counter()
        result = h_index(citations)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{' '.join(map(str, citations))}', t_end, memory, result])

    def test_str_sort3(self):
        # given
        citations = [randint(1, 5000) for i in range(1000)]
        expected_result = hindex(citations)

        # when
        t_start = time.perf_counter()
        result = h_index(citations)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{' '.join(map(str, citations[:4]))}', t_end, memory, result])
        print()
        print(Style.BRIGHT + 'Lab #3 | Task #5 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()