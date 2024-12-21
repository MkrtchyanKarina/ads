import unittest
import psutil
import time
from utils import table
from lab3.task3.src.task3 import scarecrow_sort
from random import randint
from colorama import Style

expected_time = 2
expected_memory = 256


class ScarecrowSortTest(unittest.TestCase):
    def test_scr_sort0(self):
        # given
        n = 1
        k = 1
        l = [2]
        expected_result = 'ДА'

        # when
        t_start = time.perf_counter()
        result = scarecrow_sort(n, k, l)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {k}\n{' '.join(map(str, l))}', t_end, memory,result])




    def test_scr_sort1(self):
        # given
        n = 3
        k = 2
        l = [2, 1, 3]
        expected_result = 'НЕТ'

        # when
        t_start = time.perf_counter()
        result = scarecrow_sort(n, k, l)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {k}\n{' '.join(map(str, l))}', t_end, memory, result])

    def test_scr_sort2(self):
        # given
        n = 9
        k = 4
        l = [1, 5, 3, 4, 1, 7, 6, 8, 2]
        expected_result = 'НЕТ'

        # when
        t_start = time.perf_counter()
        result = scarecrow_sort(n, k, l)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {k}\n{' '.join(map(str, l))}', t_end, memory, result])



    def test_scr_sort3(self):
        # given
        n = 5
        k = 3
        l = [1, 5, 3, 4, 1]
        expected_result = 'ДА'

        # when
        t_start = time.perf_counter()
        result = scarecrow_sort(n, k, l)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {k}\n{' '.join(map(str, l))}', t_end, memory, result])

    def test_scr_sort4(self):
        # given
        n = 10**5
        k = 10
        l = [randint(-10**9, 10**9) for i in range(10**5)]
        expected_result = 'НЕТ'

        # when
        t_start = time.perf_counter()
        result = scarecrow_sort(n, k, l)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {k}\n{' '.join(map(str, l[:4]))}', t_end, memory, result])
        print()
        print(Style.BRIGHT + 'Lab #3 | Task #3 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()