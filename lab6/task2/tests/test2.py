import time
import unittest
import psutil
from lab6.task2.src.task2 import PhoneBook
from utils import table
from colorama import Style
from random import randint, choice

expected_time = 6
expected_memory = 512


class TestPhoneBook(unittest.TestCase):
    def test_phone_book_0(self):
        # given
        count = 12
        actions = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910',
                   'find 911', 'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
        expected_result = ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy']

        # when
        t_start = time.perf_counter()
        result = PhoneBook(actions).distribute_actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{count}\n{'\n'.join(actions)}', t_end, memory, '\n'.join(result)])

    def test_phone_book_1(self):
        # given
        count = 8
        actions = ['find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456',
                   'del 0', 'del 0', 'find 0']
        expected_result = ['not found', 'granny', 'me', 'not found']

        # when
        t_start = time.perf_counter()
        result = PhoneBook(actions).distribute_actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{count}\n{'\n'.join(actions)}', t_end, memory, '\n'.join(result)])

    def test_phone_book_2(self):
        # given
        count = 10 ** 5
        phone_numbers = [randint(0, 10 ** 7 - 1) for _ in range(count // 2)]
        actions = [f'add {phone_numbers[i]} {''.join([chr(randint(97, 122)) for _ in range(15)])}' for i in range(count // 2)]
        actions += [f'{choice(['find', 'del'])} {phone_numbers[i]}' for i in range(count // 2)]


        # when
        t_start = time.perf_counter()
        result = PhoneBook(actions).distribute_actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{count}\n{'\n'.join(actions[:10])}', t_end, memory, '\n'.join(result[:10])])

        print()
        print(Style.BRIGHT + 'Lab #6 | Task #2 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()
