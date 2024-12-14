import unittest
import psutil
import time
from lab4.src.utils import table
from lab4.task11.src.task11 import bureaucracy
from random import randint
from colorama import Style


class BureaucracyTest(unittest.TestCase):
    def test_bureaucracy_0(self):
        # given
        visitors_count = 3
        documents_count = 2
        queue = [1, 2, 3]
        expected_result = (2, [3, 1])


        # when
        t_start = time.perf_counter()
        result = bureaucracy(visitors_count, documents_count, queue)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{visitors_count} {documents_count}\n{' '.join(map(str, queue))}',
                       t_end, memory, f'{result[0]}\n{' '.join(map(str, result[1]))}'])

    def test_bureaucracy_1(self):
        # given
        visitors_count = 4
        documents_count = 5
        queue = [2, 5, 2, 3]
        expected_result = (3, [4, 1, 2])


        # when
        t_start = time.perf_counter()
        result = bureaucracy(visitors_count, documents_count, queue)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{visitors_count} {documents_count}\n{' '.join(map(str, queue))}',
                       t_end, memory, f'{result[0]}\n{' '.join(map(str, result[1]))}'])

    def test_bureaucracy_2(self):
        # given
        visitors_count = 8
        documents_count = 16
        queue = [2, 1, 1, 3, 2, 4, 2, 1]
        expected_result = (-1, [])

        # when
        t_start = time.perf_counter()
        result = bureaucracy(visitors_count, documents_count, queue)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{visitors_count} {documents_count}\n{' '.join(map(str, queue))}',
                       t_end, memory, f'{result[0]}\n{' '.join(map(str, result[1]))}'])

    def test_bureaucracy_3(self):
        # given
        visitors_count = 10**5
        documents_count = 10**7  # чтобы "выдать" 10^9 документов понадобится более 10^9 / 10^7 = 100 секунд
        queue = [randint(1, 10**6) for _ in range(visitors_count)]


        # when
        t_start = time.perf_counter()
        result = bureaucracy(visitors_count, documents_count, queue)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        table.add_row(["Значения из примера", f'{visitors_count} {documents_count}\n{' '.join(map(str, queue[:3]))}',
                       t_end, memory, f'{result[0]}\n{' '.join(map(str, result[1][:3]))}'])
        print()
        print(Style.BRIGHT + 'Task #11 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()