from utils import File
import typing as tp


def net_packet_processing(buffer_size: int, packages_count: int, packages: tp.List[tp.Tuple[int, int]]) -> tp.List[int]:
    if packages_count == 0:
        return []
    deque = []
    result = []
    head = 0
    buffer_time = packages[0][0]
    for p in packages:
        start_time, duration = p
        head = max([head] + [index for index in range(len(deque)) if deque[index] <= start_time])
        if len(deque[head + 1:]) < buffer_size:
            result += [max(buffer_time, start_time)]
            buffer_time += duration
            deque.append(buffer_time)
        else:
            result += [-1]
    return result


def limits(buffer_size: int, packages_count: int, packages: tp.List[tp.Tuple[int, int]]) -> bool:
    if (1 <= buffer_size <= 10 ** 5) and (1 <= packages_count <= 10 ** 5) and all(
            0 <= a <= 10 ** 6 and 0 <= p <= 10 ** 3 for a,
            p in packages):
        return True
    else:
        return False


def net_packet_processing_txt():
    f = File(__file__)
    arguments = f.read()
    buffer_size, packages_count = list(map(int, arguments[0].split(" ")))
    packages = []
    for i in range(1, packages_count + 1):
        a, p = list(map(int, arguments[i].split(" ")))
        packages += [(a, p)]

    if limits(buffer_size, packages_count, packages):
        res = "\n".join(map(str, net_packet_processing(buffer_size, packages_count, packages)))
        f.write(res)


if __name__ == "__main__":
    net_packet_processing_txt()
