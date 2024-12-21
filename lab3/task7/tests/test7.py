import string
import unittest
import psutil
import time
from random import choice
from utils import table
from lab3.task7.src.task7 import strings_sort, reformat
from colorama import Style

expected_time = 3
expected_memory = 256


def create_array(n: int, m: int):
    alf = string.ascii_lowercase
    strings = [''.join([choice(alf) for j in range(m)]) for i in range(n)]
    return strings


def check(n, m, k, strings):
    strings = reformat(n, strings)
    for ind in range(m - 1, m - k - 1, -1):
        strings = sorted(strings, key=lambda x: x[1][ind])
    return [s[0] for s in strings]


def arr_to_str(arr):
    return ' '.join(str(x) for x in arr[:3])



class StringsSortTest(unittest.TestCase):

    def test_str_sort0(self):
        # given
        n = 1
        m = 1
        k = 1
        strings = create_array(n, m)
        expected_result = check(n, m, k, strings)

        # when
        t_start = time.perf_counter()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {m} {k}\n{arr_to_str(strings)}', t_end, memory, arr_to_str(result)])

    def test_str_sort1(self):
        # given
        n = 3
        m = 3
        k = 2
        strings = ['bbb', 'aba', 'baa']
        expected_result = check(n, m, k, strings)

        # when
        t_start = time.perf_counter()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n} {m} {k}\n{arr_to_str(strings)}', t_end, memory, arr_to_str(result)])


    def test_str_sort2(self):
        # given
        n = 5*10**3
        m = 10**4
        k = 1000
        strings = create_array(n, m)

        # when
        t_start = time.perf_counter()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{n} {m} {k}\n{arr_to_str([x[:3] for x in strings[:3]])}', t_end,
                       memory, arr_to_str(result)])
        print()
        print(Style.BRIGHT + 'Lab #3 | Task #7 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()