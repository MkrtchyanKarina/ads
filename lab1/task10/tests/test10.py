import unittest

from colorama import Style

from lab1.task10.src.task10 import palindrome
import psutil
import time
from lab1.src.utils import table
from random import randint

expected_time = 1
expected_memory = 64


class PalindromeTestCase(unittest.TestCase):
    def test_palindrome_0(self):


        # given
        length = 10
        string = "ABDRBCANOR"
        expected_result = "ABRCRBA"

        # when
        t_start = time.perf_counter()
        result = palindrome(length, string)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{length}\n{string[:10]}", t_end, memory, result[:10]])



    def test_palindrome_1(self):
        # given
        length = 3
        string = "AAB"
        expected_result = "ABA"

        # when
        t_start = time.perf_counter()
        result = palindrome(length, string)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{length}\n{string[:10]}", t_end, memory, result[:10]])


    def test_palindrome_2(self):
        # given
        length = 6
        string = "QAZQAZ"
        expected_result = "AQZZQA"

        # when
        t_start = time.perf_counter()
        result = palindrome(length, string)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{length}\n{string[:10]}", t_end, memory, result[:10]])

    def test_palindrome_3(self):
        # given
        length = 6
        string = "ABCDEF"
        expected_result = "arr_a"

        # when
        t_start = time.perf_counter()
        result = palindrome(length, string)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{length}\n{string[:10]}", t_end, memory, result[:10]])

    def test_palindrome_4(self):
        # given
        length = 10**5
        string = "".join(chr(randint(65, 90)) for _ in range(length))

        # when
        t_start = time.perf_counter()
        result = palindrome(length, string)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f"{length}\n{string[:10]}", t_end, memory, result[:10]])

        print()
        print(Style.BRIGHT + 'Task #10 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()