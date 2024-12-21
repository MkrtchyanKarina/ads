from lab3.task9.src.task9 import shortest_distance, slow_shortest_distance, Dot
import time
import psutil
import unittest
from random import randint
from utils import table
from colorama import Style

expected_time = 10
expected_memory = 256


class ShortestDistanceTest(unittest.TestCase):
    def test_shortest_distance0(self):
        # given
        n = 1
        array = [(7, 7)]
        m = [Dot(x, y) for x, y in array]
        expected_result = slow_shortest_distance(n, m)

        # when
        t_start = time.perf_counter()
        result = shortest_distance(n, m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance1(self):
        # given
        n = 4
        array = [(7, 7), (1, 100), (4, 8), (7, 7)]
        m = [Dot(x, y) for x, y in array]
        expected_result = slow_shortest_distance(n, m)

        # when
        t_start = time.perf_counter()
        result = shortest_distance(n, m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance2(self):
        # given
        n = 2
        array = [(0, 0), (3, 4)]
        m = [Dot(x, y) for x, y in array]
        expected_result = slow_shortest_distance(n, m)

        # when
        t_start = time.perf_counter()
        result = shortest_distance(n, m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance3(self):
        # given
        n = 10**5
        start, end = -10**9, 10**9
        array = [(randint(start, end), randint(start, end)) for i in range(n)]
        m = [Dot(x, y) for x, y in array]

        # when
        t_start = time.perf_counter()
        result = shortest_distance(n, m)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения", f'{n}\n{" ".join(map(str, array[:2]))}...', t_end, memory,result])
        print()
        print(Style.BRIGHT + 'Lab #3 | Task #9 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()