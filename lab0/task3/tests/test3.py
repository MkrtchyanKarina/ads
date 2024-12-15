import unittest
import psutil
import time
from lab0.src.utils import table
from lab0.task3.src.task3 import fib_number
from colorama import Style


expected_time = 1
expected_memory = 64


class FibNumberTest(unittest.TestCase):

    def test_fib_number_0(self):
        # given
        number = 10
        expected_result = 55

        # when
        t_start = time.perf_counter()
        result = fib_number(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])


    def test_fib_number_1(self):
        # given
        number = 100
        expected_result = 354224848179261915075

        # when
        t_start = time.perf_counter()
        result = fib_number(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])



    def test_fib_number_2(self):
        # given
        number = 199
        expected_result = 173402521172797813159685037284371942044301

        # when
        t_start = time.perf_counter()
        result = fib_number(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])



    def test_fib_number_3(self):
        # given
        number = 2*10**4

        # when
        t_start = time.perf_counter()
        result = fib_number(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", number, t_end, memory,  str(result)[:40] + "..."])

        print()
        print(Style.BRIGHT + 'Lab #0 | Task #3 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
