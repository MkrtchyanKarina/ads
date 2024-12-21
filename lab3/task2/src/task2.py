from utils import File


def worst_case(n: int) -> list[int]:
    worst_arr = [i + 1 for i in range(n)]
    for i in range(2, len(worst_arr)):
        worst_arr[i], worst_arr[i // 2] = worst_arr[i // 2], worst_arr[i]
    return worst_arr


def limits(n: int) -> bool:
    if 1 <= n <= 10**6:
        return True
    else:
        return False


def worst_case_txt():
    f = File(__file__)
    arguments = f.read()
    n = int(arguments[0])

    if limits(n):
        res = " ".join(map(str, worst_case(n)))
        f.write(res)



if __name__ == "__main__":
    worst_case_txt()