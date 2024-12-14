import time
import unittest
import psutil
from lab7.task1.src.task1 import exchange, exchange_with_amount
from lab6.src.utils import table
from colorama import Style
from random import randint

expected_time = 1
expected_memory = 64



class TestExchange(unittest.TestCase):
    def test_exchange_0(self):
        # given
        money = 10**5
        amount = 100
        coins = [randint(1, 10**3) for _ in range(amount)]


        # when
        t_start = time.perf_counter()
        result = exchange(money, coins)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{money} {amount}\n', t_end, memory, result])



    def test_exchange_1(self):
        # given
        money = 10**5
        amount = 100
        coins = {randint(1, 10**3) : randint(1, 10) for _ in range(amount)}


        # when
        t_start = time.perf_counter()
        result = exchange_with_amount(money, coins)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера", f'{money} {amount}\n', t_end, memory, result])



        print()
        print(Style.BRIGHT + 'Task #1 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()