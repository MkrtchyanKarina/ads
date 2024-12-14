from lab4.src.utils import File


def bracket_sequence(brackets: str):
    bracket_pairs = {')': '(',
                     '}': '{',
                     ']': '['}
    if len(brackets) == 1:
        symbol = brackets[0]
        if symbol in bracket_pairs.keys() or symbol in bracket_pairs.values():
            return "1"
        else:
            return "Success"
    else:
        stack = ""
        err_ind = 1
        for b in brackets:
            if b in bracket_pairs.values() or len(stack) == 0:
                stack += b
            elif b in bracket_pairs.keys():
                if bracket_pairs[b] == stack[-1]:
                    stack = stack[:-1]
                else:
                    return str(err_ind)
            else:
                pass
            err_ind += 1
    return "Success"


def limits(brackets: str) -> bool:
    if 1 <= len(brackets) <= 10**5:
        return True
    else:
        return False


def bracket_sequence_txt():
    f = File(__file__)
    data = f.read()
    brackets = data[0]
    if limits(brackets):
        f.write(bracket_sequence(brackets))


if __name__ == "__main__":
    bracket_sequence_txt()
    print(bracket_sequence('foo(bar[index);'))