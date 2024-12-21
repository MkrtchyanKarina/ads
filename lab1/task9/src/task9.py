from utils import File


def binary_addition(binary1: str, binary2: str) -> str:
    binary1 = [int(i) for i in binary1]
    binary2 = [int(i) for i in binary2]
    n = len(binary1)
    c = [int(i) for i in "0"*(n+1)]
    for i in range(1, n+1):
        s = binary1[-i] + binary2[-i] + c[-i]
        c[-i - 1] = s // 2
        c[-i] = s % 2
    binary_sum = "".join(map(str, c))
    binary_sum = binary_sum[binary_sum.index("1"):]
    return binary_sum


def limits(binary1: str, binary2: str) -> bool:
    if (all(b in "01" for b in binary1) and all(b in "01" for b in binary2) and
            (1 <= len(binary1) == len(binary2) <= 10**3)):
        return True
    else:
        return False


def binary_addition_txt():
    f = File(__file__)
    arguments = f.read()[0]
    binary1, binary2 = arguments.split(" ")
    if limits(binary1, binary2):
        res = binary_addition(binary1, binary2)
        f.write(res)


if __name__ == "__main__":
    binary_addition_txt()


