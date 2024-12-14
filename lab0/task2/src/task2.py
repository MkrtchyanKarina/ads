from lab0.src.utils import File


def addition_sqrt(first_term: int, second_term: int) -> int:
    return first_term + second_term ** 2



def limits(first_term: int, second_term: int) -> bool:
    if abs(first_term) <= 10**9 and abs(second_term) <= 10**9:
        return True
    else:
        return False


def addition_sqrt_txt():
    f = File(__file__)
    arguments = f.read()
    first_term, second_term = map(int, arguments[0].split(" "))
    if limits(first_term, second_term):
        res = str(addition_sqrt(first_term, second_term))
        f.write(res)


if __name__ == "__main__":
    addition_sqrt_txt()
