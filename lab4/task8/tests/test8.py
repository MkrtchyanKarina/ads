import unittest
import psutil
import time
from utils import table
from lab4.task8.src.task8 import equal
from random import randint, choice
from colorama import Style

expected_time = 2
expected_memory = 256


class EqualTest(unittest.TestCase):
    def test_equal_0(self):
        # given
        actions_count = 7
        expression = "8 9 + 1 7 - *"
        expected_result = -102


        # when
        t_start = time.perf_counter()
        result = equal(expression)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{actions_count}\n{expression}', t_end, memory, result])

    def test_equal_1(self):
        # given
        actions_count = 9
        expression = "5 15 + 4 7 + 1 - /"
        expected_result = 2


        # when
        t_start = time.perf_counter()
        result = equal(expression)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{actions_count}\n{expression}', t_end, memory, result])

    def test_equal_2(self):
        # given
        actions_count = 8
        expression = "5 15 + 4 7 + 1 -"
        expected_result = "error"


        # when
        t_start = time.perf_counter()
        result = equal(expression)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{actions_count}\n{expression}', t_end, memory, result])

    def test_equal_3(self):
        # given
        actions_count = 10**5
        start = f'{randint(-10, 10)} {randint(-10, 10)} {choice(['+', '-', '*'])} ' * 2 + f'{choice(['+', '-', '*'])} '
        middle = f'{randint(-10, 10)} {randint(-10, 10)} {choice(['+', '-', '*'])} {choice(['+', '-', '*'])} ' * (actions_count // 4)
        middle = middle[:-1]
        expression = start + middle


        # when
        t_start = time.perf_counter()
        result = equal(expression)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        if result > 10**9:
            result //= 10**9
        table.add_row(["Значения из примера", f'{actions_count}\n{expression[:7]}', t_end, memory, result])
        print()
        print(Style.BRIGHT + 'Lab #4 | Task #8 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()