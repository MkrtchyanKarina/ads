from utils import File


def addition(first_term: int, second_term: int) -> int:
    return first_term + second_term



def limits(first_term: int, second_term: int) -> bool:
    if abs(first_term) <= 10**9 and abs(second_term) <= 10**9:
        return True
    else:
        return False


def addition_txt():
    f = File(__file__)
    arguments = f.read()
    first_term, second_term = map(int, arguments[0].split(" "))
    if limits(first_term, second_term):
        res = str(addition(first_term, second_term))
        f.write(res)


if __name__ == "__main__":
    addition_txt()
