import time
import unittest
import psutil
from lab6.task1.src.task1 import HashTable
from lab6.src.utils import table
from colorama import Style
from random import randint, choice

expected_time = 2
expected_memory = 256



class TestHashTable(unittest.TestCase):
    def test_hash_table_0(self):
        # given
        array_len = 6
        array = ['arr_a 5', 'arr_a 3', 'D 2', 'D 3', '? 3', '? 5']
        expected_result = ['N', 'Y']

        # when
        t_start = time.perf_counter()
        result = HashTable(array).actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{'\n'.join(array)}', t_end, memory, '\n'.join(result)])


    def test_hash_table_1(self):
        # given
        array_len = 13
        array = ['arr_a 5', 'arr_a 3', 'D 2', 'D 3', '? 3', '? 5', 'arr_a 8', 'arr_a 8', '? 8', 'D 8', '? 8', 'D 8', '? 8']
        expected_result = ['N', 'Y', 'Y', 'N', 'N']

        # when
        t_start = time.perf_counter()
        result = HashTable(array).actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{'\n'.join(array)}', t_end, memory, '\n'.join(result)])


    def test_hash_table_2(self):
        # given
        array_len = 5 * 10 ** 5
        array = [f'{choice(['arr_a', 'D', '?'])} {randint(-10**18, 10**18)}' for _ in range(array_len)]

        # when
        t_start = time.perf_counter()
        result = HashTable(array).actions()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{array_len}\n{'\n'.join(array[:4])}', t_end, memory, '\n'.join(result[:4])])

        print()
        print(Style.BRIGHT + 'Lab #6 | Task #1 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()