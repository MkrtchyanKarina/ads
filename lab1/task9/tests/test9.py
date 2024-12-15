import unittest
from random import randint
from colorama import Style
from lab1.task9.src.task9 import binary_addition
import psutil
import time
from lab1.src.utils import table

expected_time = 1
expected_memory = 64


class BinaryAdditionTestCase(unittest.TestCase):

    def test_binary_addition_1(self):
        # given
        a, b = "1", "1"
        expected_result = "10"

        # when
        t_start = time.perf_counter()
        result = binary_addition(a, b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f"{a[:10]}\n{b[:10]}", t_end, memory, result[:11]])

    def test_binary_addition_2(self):
        # given
        a, b = "111000", "010101"
        expected_result = bin(int(a, 2) + int(b, 2))[2:]

        # when
        t_start = time.perf_counter()
        result = binary_addition(a, b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{a[:10]}\n{b[:10]}", t_end, memory, result[:11]])

    def test_binary_addition_3(self):
        # given
        length = 100
        a = "".join(map(str, [randint(0, 1) for _ in range(length)]))
        b = "".join(map(str, [randint(0, 1) for _ in range(length)]))
        expected_result = bin(int(a, 2) + int(b, 2))[2:]

        # when
        t_start = time.perf_counter()
        result = binary_addition(a, b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{a[:10]}\n{b[:10]}", t_end, memory, result[:11]])

    def test_binary_addition_4(self):
        # given
        length = 10**3
        a = "".join(map(str, [randint(0, 1) for _ in range(length)]))
        b = "".join(map(str, [randint(0, 1) for _ in range(length)]))
        expected_result = bin(int(a, 2) + int(b, 2))[2:]

        # when
        t_start = time.perf_counter()
        result = binary_addition(a, b)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f"{a[:10]}\n{b[:10]}", t_end, memory, result[:11]])

        print()
        print(Style.BRIGHT + 'Lab #1 | Task #9 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()