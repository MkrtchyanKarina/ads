import typing as tp
from utils import File


class MergeSortActions:
    def __init__(self):
        self.actions = ""


    def merge_sort(self, start: int, end: int, array: tp.List[int]) -> tp.List[int]:
        middle = (start + end + 1) // 2
        list_a, list_b = array[start:middle], array[middle:end + 1]

        len_a, len_b = middle - start, end + 1 - middle
        if len_a > 1:
            list_a = self.merge_sort(start, middle - 1, array)
        if len_b > 1:
            list_b = self.merge_sort(middle, end, array)
        return self.merge(start, end, list_a, list_b)

    def merge(self, start: int, end: int, array_a: tp.List[int], array_b:  tp.List[int]) -> tp.List[int]:

        array_c = []
        index_a, index_b = 0, 0
        for i in range(end - start + 1):
            if index_b == len(array_b):
                array_c.extend(array_a[index_a:])
                break
            elif index_a == len(array_a):
                array_c.extend(array_b[index_b:])
                break
            else:
                if array_a[index_a] <= array_b[index_b]:
                    array_c.append(array_a[index_a])
                    index_a += 1
                else:
                    array_c.append(array_b[index_b])
                    index_b += 1
        self.actions += f'{start+1} {end+1} {" ".join(map(str, array_c))}\n'

        return array_c


    def return_actions(self) -> str:
        a = self.actions.split('\n')[:-1]
        a[-1] = a[-1][5:]
        return '\n'.join(a)


def limits(n: int, m: list[int]) -> bool:
    if 1 <= n <= 10**5 and len(m) == n and all(abs(x) <= 10**9 for x in m):
        return True
    else:
        return False


def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        ex = MergeSortActions()
        ex.merge_sort(0, array_len, array)
        res = ex.return_actions()
        f.write(res)


if __name__ == "__main__":
    quick_sort_txt()