from lab1.task4.src.task4 import lineal_search
import unittest
import psutil
import time
from random import randint
from lab1.src.utils import table
from colorama import Style


expected_time = 1
expected_memory = 64


class LinealSearch(unittest.TestCase):
    def test_lineal_search_0(self):
        # given
        array = [133, 14, 234, 15, 15, 78, 15, 98]
        element = 15
        expected_result = (3, [3, 4, 6])

        # when
        t_start = time.perf_counter()
        result = lineal_search(array, element)
        count, indexes = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{' '.join(map(str, array))}\n{element}', t_end, memory,
                       f"{count}\n{' '.join(map(str, indexes))}"])


    def test_lineal_search_1(self):
        # given
        array_len = 100
        array = [randint(-array_len, array_len) for _ in range(array_len)]
        element = array[randint(0, array_len-1)]

        # when
        t_start = time.perf_counter()
        result = lineal_search(array, element)
        count, indexes = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{' '.join(map(str, array[:5]))}\n{element}', t_end, memory,
                       f"{count}\n{' '.join(map(str, indexes[:5]))}"])


    def test_lineal_search_2(self):
        # given
        array_len = 10**3
        array = [randint(-array_len, array_len) for _ in range(array_len)]
        element = array[randint(0, array_len-1)]

        # when
        t_start = time.perf_counter()
        result = lineal_search(array, element)
        count, indexes = result
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{' '.join(map(str, array[:5]))}\n{element}', t_end, memory,
                       f"{count}\n{' '.join(map(str, indexes[:5]))}"])

        print()
        print(Style.BRIGHT + 'Lab #1 | Task #4 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
