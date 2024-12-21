import unittest
import psutil
import time
from utils import table
from lab5.task3.src.task3 import net_packet_processing
from random import randint
from colorama import Style

expected_time = 10
expected_memory = 512


class TestNetworkPacketProcessing(unittest.TestCase):

    def test_should_processing_0(self):

        # given
        expected_result = [0, 2, 4, 6, 8, -1]
        data = (3, 6, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])

        # when
        t_start = time.time()
        result = net_packet_processing(data[0], data[1], data[2])
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])





    def test_should_processing_1(self):

        # given
        expected_result = [0, 3, 10]
        data = (2, 3, [(0, 1), (3, 1), (10, 1)])

        # when
        t_start = time.time()
        result = net_packet_processing(data[0], data[1], data[2])
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])




    def test_should_processing_2(self):

        # given
        expected_result = [0, 2]
        data = (1, 2, [(0, 1), (2, 1)])

        # when
        t_start = time.time()
        result = net_packet_processing(data[0], data[1], data[2])
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])




    def test_should_processing_3(self):

        # given
        expected_result = [0]
        data = (1, 1, [(0, 0)])

        # when
        t_start = time.time()
        result = net_packet_processing(data[0], data[1], data[2])
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Значения из примера","\n".join(str(d) for d in data), t_end, memory," ".join(map(str, result))])




    def test_should_processing_time_test(self):

        # given

        size = 1000
        count = 10**5
        packages = sorted([(c+ 10, randint(0, 10**3)) for c in range(count)])
        data = (size, count, packages)



        # when
        t_start = time.time()
        result = net_packet_processing(data[0], data[1], data[2])
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(memory, expected_memory)
        table.add_row(["Максимальные значения",f'{size}\n{count}\n{packages[count-5:]}', t_end, memory, " ".join(map(str, result[count-5:]))])
        print()
        print(Style.BRIGHT + 'Lab #5 | Task #3 - Test Table' + Style.RESET_ALL)
        print(table)
        table.clear_rows()


if __name__ == '__main__':
    unittest.main()