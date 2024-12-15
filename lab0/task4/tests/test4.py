from lab0.task4.src.task4 import last_digit
import unittest
import psutil
import time
from lab0.src.utils import table
from colorama import Style


expected_time = 5
expected_memory = 512



class LastDigitTest(unittest.TestCase):

    def test_last_digit_0(self):
        # given
        number = 0
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = last_digit(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])

    def test_last_digit_1(self):
        # given
        number = 10
        expected_result = 5

        # when
        t_start = time.perf_counter()
        result = last_digit(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])

    def test_last_digit_2(self):
        # given
        number = 331
        expected_result = 9

        # when
        t_start = time.perf_counter()
        result = last_digit(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])

    def test_last_digit_3(self):
        # given
        number = 327305
        expected_result = 5

        # when
        t_start = time.perf_counter()
        result = last_digit(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])

    def test_last_digit_4(self):
        # given
        number = 10**7

        # when
        t_start = time.perf_counter()
        result = last_digit(number)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", number, t_end, memory,  result])

        print()
        print(Style.BRIGHT + 'Lab #0 | Task #4 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()
