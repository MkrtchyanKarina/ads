import unittest
import psutil
import time
from utils import table
from lab4.task6.src.task6 import queue_actions
from random import randint, choice
from colorama import Style

expected_time = 2
expected_memory = 256


class BracketSequenceTest(unittest.TestCase):
    def test_queue_actions_0(self):
        # given
        commands_count = 7
        commands = ['+ 1', '?', '+ 10', '?', '-', '?', '-']
        expected_result = [1, 1, 10]


        # when
        t_start = time.perf_counter()
        result = queue_actions(commands)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{commands_count}\n{'\n'.join(commands)}', t_end, memory, '\n'.join(map(str, result))])


    def test_queue_actions_1(self):
        # given
        commands_count = 9
        commands = ['+ 21', '+ 10', '+ 13', '?', '-', '-', '+ 4', '?', '-']
        expected_result = [10, 4]


        # when
        t_start = time.perf_counter()
        result = queue_actions(commands)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{commands_count}\n{'\n'.join(commands)}', t_end, memory, '\n'.join(map(str, result))])

    def test_queue_actions_2(self):
        # given
        commands_count = 10**6
        commands = ([f'+ {randint(-10**9, 10**9)}' for _ in range(commands_count // 2)]
                    + [choice([f'+ {randint(-10**9, 10**9)}', '-', '?']) for _ in range(commands_count // 2)])

        # when
        t_start = time.perf_counter()
        result = queue_actions(commands)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{commands_count}\n{'\n'.join(commands[-5:])}',
                       t_end, memory, '\n'.join(map(str, result[-5:]))])
        print()
        print(Style.BRIGHT + 'Lab #4 | Task #6 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()