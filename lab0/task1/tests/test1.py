import unittest
import psutil
import time
from random import randint
from lab0.src.utils import table
from lab0.task1.src.task1 import addition
from colorama import Style


expected_time = 1
expected_memory = 64


class AdditionTest(unittest.TestCase):

    def test_addition_0(self):
        # given
        first_term = 12
        second_term = 25
        expected_result = 37

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{first_term} {second_term}', t_end, memory,  result])


    def test_addition_1(self):
        # given
        first_term = 130
        second_term = 61
        expected_result = 191

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{first_term} {second_term}', t_end, memory,  result])

    def test_addition_2(self):
        # given
        first_term = -130
        second_term = 30
        expected_result = -100

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{first_term} {second_term}', t_end, memory,  result])

    def test_addition_3(self):
        # given
        first_term = -130
        second_term = -24
        expected_result = -154

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{first_term} {second_term}', t_end, memory,  result])

    def test_addition_4(self):
        # given
        first_term = 30
        second_term = -24
        expected_result = 6

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{first_term} {second_term}', t_end, memory,  result])


    def test_addition_5(self):
        # given
        first_term = randint(-10**9, 10**9)
        second_term = randint(-10**9, 10**9)
        expected_result = first_term + second_term

        # when
        t_start = time.perf_counter()
        result = addition(first_term, second_term)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{first_term} {second_term}', t_end, memory,  result])

        print()
        print(Style.BRIGHT + 'Task #1 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
