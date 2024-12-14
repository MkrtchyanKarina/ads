import time
import unittest
import psutil
from lab6.task5.src.task5 import elections
from lab6.src.utils import table
from colorama import Style
from random import randint

expected_time = 2
expected_memory = 64



class ElectionsTable(unittest.TestCase):
    def test_elections_0(self):
        # given
        states_result = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expected_result = ['ivanov 900', 'petr 70', 'tourist 3']

        # when
        t_start = time.perf_counter()
        result = elections(states_result)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", '\n'.join(states_result), t_end, memory, '\n'.join(result)])

    def test_elections_1(self):
        # given
        states_result = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expected_result = ['McCain 16', 'Obama 17']

        # when
        t_start = time.perf_counter()
        result = elections(states_result)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", '\n'.join(states_result), t_end, memory, '\n'.join(result)])


    def test_elections_2(self):
        # given
        states_result = ['bur 1']
        expected_result = ['bur 1']

        # when
        t_start = time.perf_counter()
        result = elections(states_result)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", '\n'.join(states_result), t_end, memory, '\n'.join(result)])


    def test_elections_3(self):
        # given
        states_result = [f'{''.join([chr(randint(97, 122)) for _ in range(15)])} {randint(0, 10**18)}'
                         for _ in range(10**5)]

        # when
        t_start = time.perf_counter()
        result = elections(states_result)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", '\n'.join(states_result[:10]), t_end, memory, '\n'.join(result[:10])])


        print()
        print(Style.BRIGHT + 'Task #5 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()