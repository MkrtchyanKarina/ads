import unittest
import psutil
import time
from lab4.src.utils import table
from lab4.task13_3.src.task13_3 import LinkedList, Node
from colorama import Style


class LinkedListTest(unittest.TestCase):
    def test_LL_0(self):
        # given
        ll = LinkedList(root=None)
        expected_result = []

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nis_empty()', t_end, memory, f'{result}'])


    def test_LL_1(self):
        # given
        root = Node(10)
        ll = LinkedList(root)
        ll.prepend(13)
        ll.prepend(12)
        ll.popleft()
        ll.prepend(19)

        expected_result = [19, 13, 10]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nprepend(), popleft()', t_end, memory, f'{result}'])


    def test_LL_2(self):
        # given
        root = Node(19)
        ll = LinkedList(root)
        ll.insert_after(19, 8)
        ll.insert_after(19, 18)
        ll.insert_after(8, 7)
        ll.insert_after(18, 17)
        ll.insert_after(17, 9)
        expected_result = [19, 18, 17, 9, 8, 7]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\ninsert_after()', t_end, memory, f'{result}'])


    def test_LL_3(self):
        # given
        root = Node(19)
        ll = LinkedList(root)
        ll.delete_after(19)
        expected_result = [19]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\ndelete_after()', t_end, memory, f'{result}'])

    def test_LL_4(self):
        # given
        root = Node(16)
        ll = LinkedList(root)
        ll.delete_after(19)
        expected_result = [16]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\ndelete_after()', t_end, memory, f'{result}'])

    def test_LL_5(self):
        # given
        root = Node(16)
        ll = LinkedList(root)
        ll.prepend(17)
        ll.prepend(18)
        ll.prepend(19)
        ll.prepend(20)
        ll.prepend(21)
        ll.delete_after(21)
        ll.delete_after(20)
        ll.delete_after(18)
        expected_result = [21, 19, 18, 16]

        # when
        t_start = time.perf_counter()
        result = ll.output()
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\ndelete_after()', t_end, memory, f'{result}'])

    def test_LL_6(self):
        # given
        root = Node(16)
        ll = LinkedList(root)
        ll.prepend(17)
        ll.prepend(18)
        ll.prepend(19)
        ll.prepend(20)
        ll.prepend(21)

        expected_result = True

        # when
        t_start = time.perf_counter()
        result = ll.search(18)
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nsearch(18)', t_end, memory, f'{result}'])

    def test_LL_7(self):
        # given
        root = Node(16)
        ll = LinkedList(root)
        ll.prepend(17)
        ll.prepend(18)
        ll.prepend(19)
        ll.prepend(20)
        ll.prepend(21)

        expected_result = False

        # when
        t_start = time.perf_counter()
        result = ll.search('Hello')
        t_end = round(time.perf_counter() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        table.add_row(["Значения из примера", f'{ll.output()}\nsearch(''Hello'')', t_end, memory, f'{result}'])

        print()
        print(Style.BRIGHT + 'Lab #4 | Task #13.3 - Test Table' + Style.RESET_ALL)
        print()
        print(table)
        table.clear_rows()


if __name__ == "__main__":
    unittest.main()