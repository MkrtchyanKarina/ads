import unittest
import psutil
import time
from utils import table
from lab4.task13_1.src.task13_1 import LinkedList, Node
from colorama import Style


class LinkedListTest(unittest.TestCase):
    def test_LL_0(self):
        # given
        ll = LinkedList(root=None)
        expected_result = True

        # when
        t_start = time.perf_counter()
        result = ll.is_empty()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nis_empty()', t_end, memory, f'{result}'])


    def test_LL_1(self):
        # given
        root = Node(10)
        ll = LinkedList(root)
        ll.push(13)
        ll.push(12)
        expected_result = [10, 13, 12]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\noutput()', t_end, memory, f'{result}'])


    def test_LL_2(self):
        # given
        root = Node(9)
        ll = LinkedList(root)
        ll.push(2)
        ll.push(25)
        ll.push(17)
        ll.push(14)
        ll.pop()
        ll.push(12)
        ll.push(15)
        ll.pop()
        expected_result = [9, 2, 25, 17, 12]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\npop()', t_end, memory, f'{result}'])


    def test_LL_3(self):
        # given
        root = Node(9)
        ll = LinkedList(root)
        ll.push(13)
        ll.push(98)
        ll.pop()
        ll.pop()
        ll.pop()
        expected_result = True

        # when
        t_start = time.perf_counter()
        result = ll.is_empty()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nis_empty()', t_end, memory, f'{result}'])

    def test_LL_4(self):
        # given
        root = Node(789)
        ll = LinkedList(root)
        ll.push(313)
        ll.push(98)
        ll.push(189)
        expected_result = [789, 313, 98, 189]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\npush()', t_end, memory, f'{result}'])
        print()
        print(Style.BRIGHT + 'Lab #4 | Task #13.1 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()