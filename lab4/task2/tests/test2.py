import unittest
import psutil
import time
from lab4.src.utils import table
from lab4.task2.src.task2 import queue_actions
from random import randint
from colorama import Style

expected_time = 2
expected_memory = 256


class QueueActionsTest(unittest.TestCase):

    def test_queue_actions_0(self):
        # given
        actions_count = 5
        actions = ['+ 2', '-', '+ 5', '+ 9', '-']
        expected_result = ['2', '5']

        # when
        t_start = time.perf_counter()
        result = queue_actions(actions)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{actions_count}\n{'\n'.join(actions)}', t_end, memory, '\n'.join(result)])

    def test_queue_actions_1(self):
        # given
        actions_count = 4
        actions = ['+ 1', '+ 10', '-', '-']
        expected_result = ['1', '10']

        # when
        t_start = time.perf_counter()
        result = queue_actions(actions)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{actions_count}\n{'\n'.join(actions)}', t_end, memory, '\n'.join(result)])

    def test_queue_actions_2(self):
        # given
        actions_count = 10**6
        actions = ([f'+ {randint(-10**9, 10**9)}' for _ in range(actions_count//2)] +
                   [f'+ {randint(-10**9, 10**9)}' if randint(0, 1) else '-' for _ in range(actions_count//2)])

        # when
        t_start = time.perf_counter()
        result = queue_actions(actions)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{actions_count}\n{'\n'.join(actions[-5:])}',
                       t_end, memory, '\n'.join(result[-5:])])
        print()
        print(Style.BRIGHT + 'Task #2 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()