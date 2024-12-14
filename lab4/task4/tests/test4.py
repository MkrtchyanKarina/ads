import unittest
import psutil
import time
from lab4.src.utils import table
from lab4.task4.src.task4 import bracket_sequence
from random import choice, randint
from colorama import Style

expected_time = 5
expected_memory = 256


class BracketSequenceTest(unittest.TestCase):
    def test_bracket_sequence_0(self):
        # given
        brackets = '[]'
        expected_result = 'Success'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_1(self):
        # given
        brackets = '{}[]'
        expected_result = 'Success'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_2(self):
        # given
        brackets = '[()]'
        expected_result = 'Success'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_3(self):
        # given
        brackets = '(())'
        expected_result = 'Success'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_4(self):
        # given
        brackets = '{'
        expected_result = '1'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_5(self):
        # given
        brackets = '{[}'
        expected_result = '3'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_6(self):
        # given
        brackets = 'foo(bar);'
        expected_result = 'Success'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_7(self):
        # given
        brackets = 'foo(bar[index);'
        expected_result = '14'


        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets, t_end, memory, result])

    def test_bracket_sequence_8(self):
        # given
        brackets_len = 10**5
        brackets = ([choice(['{', '[', '(']) for _ in range(brackets_len//2)] +
                    [chr(randint(0, 127)) for _ in range(brackets_len//2)])
        brackets = "".join(brackets)



        # when
        t_start = time.perf_counter()
        result = bracket_sequence(brackets)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", brackets[:4], t_end, memory, result])
        print()
        print(Style.BRIGHT + 'Task #4 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()