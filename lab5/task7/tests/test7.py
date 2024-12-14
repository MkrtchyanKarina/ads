import time
import unittest
from random import randint
import psutil
from lab5.task7.src.task7 import heap_sort_max
from lab5.src.utils import table
from colorama import Style

expected_time = 0.6  #  CPython выполняет около 10^7 операций в минуту => 
                    # при сложности O(visitors_count) программа должна выполняться менее 60/100 = 0.6 секунд
expected_memory = 256


class TestHeapSort(unittest.TestCase):
    def test_should_heapsort_0(self):
        # given
        n = 10**3
        array = [randint(-10**9, 10**9) for _ in range(n)]
        expected_result = sorted(array.copy())[::-1]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])




    def test_should_heapsort_1(self):
        # given
        n = 10**4
        array = [randint(-10**9, 10**9) for _ in range(n)]
        expected_result = sorted(array.copy())[::-1]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Средние значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])



    def test_should_heapsort_2(self):
        # given
        n = 10**5
        array = [randint(-10**9, 10**9) for _ in range(n)]
        expected_result = sorted(array.copy())[::-1]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])



    def test_should_heapsort_3(self):
        # given
        n = 10**5
        x, y = randint(-10**9, 10**9), randint(10**9, 10**9)
        array = [[x, y][i % 2] for i in range(n)]
        expected_result = sorted(array.copy())[::-1]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Повторяющиеся значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])

        print()
        print(Style.BRIGHT + 'Task #7 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
