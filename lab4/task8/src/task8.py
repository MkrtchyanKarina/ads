from lab4.src.utils import File
import typing as tp



def calc(a: int, b: int, action: str) -> int:
    if action == "+":
        return a + b
    elif action == "*":
        return a * b
    elif action == "-":
        return a - b
    elif action == "/":
        return int(a//b)
    else:
        return 0


def equal(expression: str) -> tp.Union[int, str]:
    expression = expression.split(" ")
    if 1 < len(expression) < 3:
        return int(expression[0])
    stack = []
    for e in expression:
        if e.isnumeric():
            stack += [int(e)]
        elif len(e) > 1 and e[1:].isnumeric():
            stack += [int(e)]
        else:
            stack[-2] = calc(stack[-2], stack[-1], e)
            stack.pop()
    if len(stack) == 1:
        return stack[0]
    else:
        return "error"


def limits(actions_count: int, expression: str) -> bool:
    if (1 <= actions_count <= 10**6) and (len(expression.split(" ")) == actions_count):
        return True
    else:
        return False


def equal_txt():
    f = File(__file__)
    data = f.read()
    actions_count = int(data[0])
    expression = data[1]
    if limits(actions_count, expression):
        f.write(str(equal(expression)))


if __name__ == "__main__":
    equal_txt()