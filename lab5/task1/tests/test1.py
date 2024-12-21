import time
import unittest
import psutil
from lab5.task1.src.task1 import is_heap
from utils import table
from random import randint
from colorama import Style

expected_time = 2
expected_memory = 256



class TestIsHeap(unittest.TestCase):
    def test_should_is_heap_args1(self):
        # given
        n = 5
        array = [1, 0, 1, 2, 0]
        expected_result = "NO"

        # when
        t_start = time.perf_counter()
        result = is_heap(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{n}\n{array}', t_end, memory, result])


    def test_should_is_heap_args2(self):
        # given
        n = 5
        array = [1, 3, 2, 5, 4]
        expected_result = "YES"

        # when
        t_start = time.perf_counter()
        result = is_heap(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{n}\n{array}', t_end, memory, result])


    def test_should_is_heap_max(self):
        # given
        n = 10**6
        array = [randint(-2*10**9, 2*10**9) for a in range(n)]
        expected_result = "NO"

        # when
        t_start = time.perf_counter()
        result = is_heap(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{n}\n{array[:3]}', t_end, memory, result])

        print()
        print(Style.BRIGHT + 'Lab #5 | Task #1 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()