import typing as tp
from lab5.src.utils import File


def heap_sort_max(high: int, array: tp.List[int]) -> tp.List[int]:
    heap = array.copy()
    build_heap(high, heap)
    for i in range(high - 1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        swap(heap, i, 0)
    return heap


def swap(heap: tp.List[int], high: int, index: int) -> None:
    left = 2 * index + 1
    right = 2 * index + 2

    if left < high and heap[left] < heap[index]:
        largest = left
    else:
        largest = index

    if right < high and heap[right] < heap[largest]:
        largest = right

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        swap(heap, high, largest)


def build_heap(high: int, heap: tp.List[int]) -> None:
    for i in range((len(heap) - 1) // 2, -1, -1):
        swap(heap, high, i)


def limits(n: int, array: tp.List[int]) -> bool:
    if (1 <= n <= 10**5) and (len(array) == n) and all(abs(x) <= 10**9 for x in array):
        return True
    else:
        return False


def heap_sort_max_txt():
    f = File(__file__)
    arguments = f.read()
    array_len = int(arguments[0])
    array = list(map(int, arguments[1].split(" ")))

    if limits(array_len, array):
        heap = heap_sort_max(array_len, array)
        res = " ".join(map(str, heap))
        f.write(res)


if __name__ == "__main__":
    heap_sort_max_txt()