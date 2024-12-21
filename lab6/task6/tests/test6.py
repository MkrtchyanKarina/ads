import time
import unittest
import psutil
from lab6.task6.src.task6 import is_fib
from utils import table
from colorama import Style

expected_time = 2
expected_memory = 128


class TestIsFib(unittest.TestCase):
    def test_should_is_fib_0(self):
        # given
        number = 5
        expected_result = "Yes"

        # when
        t_start = time.perf_counter()
        result = is_fib(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory, result])


    def test_should_is_fib_1(self):
        # given
        number = 89
        expected_result = "Yes"

        # when
        t_start = time.perf_counter()
        result = is_fib(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory, result])

    def test_should_is_fib_2(self):
        # given
        number = 610
        expected_result = "Yes"

        # when
        t_start = time.perf_counter()
        result = is_fib(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory, result])

    def test_should_is_fib_3(self):
        # given
        number = 6100
        expected_result = "No"

        # when
        t_start = time.perf_counter()
        result = is_fib(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory, result])

    def test_should_is_fib_4(self):
        # given
        number = 10**5000 - 1
        expected_result = "No"

        # when
        t_start = time.perf_counter()
        result = is_fib(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", "100000...", t_end, memory, result])

        print()
        print(Style.BRIGHT + 'Lab #6 | Task #6 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()