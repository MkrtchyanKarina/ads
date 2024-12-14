import unittest
import psutil
import time
from lab5.src.utils import table
from lab5.task4.src.task4 import MinHeap
from random import randint
from colorama import Style

expected_time = 3
expected_memory = 512


class TestHeapSortSwaps(unittest.TestCase):

    def test_should_heap_sort0(self):
        # given
        expected_result = (0, [])
        data = (5, [1, 2, 3, 4, 5])


        # when
        t_start = time.time()
        result = MinHeap(data[0], data[1]).heap_sort()
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Минимальные значения","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])

    def test_should_heap_sort1(self):
        # given
        expected_result = (3, [(1, 4), (0, 1), (1, 3)])
        data = (5, [5, 4, 3, 2, 1])

        # when
        t_start = time.time()
        result = MinHeap(data[0], data[1]).heap_sort()
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])

    def test_should_heap_sort2(self):
        # given
        n = 10**5 + 10
        array = [randint(0, 10**9) for _ in range(n)]
        array = [i for i in set(array)]
        n = len(array)


        # when
        t_start = time.time()
        result = MinHeap(n, array).heap_sort()
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения",f'{n}\n{array[:4]}', t_end, memory, f'{result[0]}\n{result[1][:4]}'])
        print()
        print(Style.BRIGHT + 'Task #4 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()