from lab4.src.utils import File
import typing as tp



def bureaucracy(visitors_count: int, documents_count: int, queue: list[int]) -> tp.Union[
                                                                                int, tp.Tuple[int, tp.List[int]]]:
    deque = queue.copy()
    head = 0
    end = visitors_count
    while documents_count > 0:
        deque[head] -= 1
        documents_count -= 1
        if deque[head] > 0:
            deque += [deque[head]]
            end += 1
        head += 1
    remainder = end - head
    return (remainder, deque[head:end]) if remainder else (-1, [])



def limits(visitors_count: int, documents_count: int, queue: list[int]) -> bool:
    if ((1 <= visitors_count == len(queue) <= 10**5) and (0 <= documents_count <= 10**9)
            and all(1 <= d <= 10**6 for d in queue)):
        return True
    else:
        return False


def bureaucracy_txt():
    f = File(__file__)
    data = f.read()
    visitors_count, documents_count = list(map(int, data[0].split(" ")))
    queue = list(map(int, data[1].split(" ")))
    if limits(visitors_count, documents_count, queue):
        result = bureaucracy(visitors_count, documents_count, queue)
        if len(result) == 1:
            f.write('-1')
        else:
            f.write(str(result[0]) + '\n' + " ".join(map(str, result[1])))


if __name__ == "__main__":
    bureaucracy_txt()