from lab4.src.utils import File
import typing as tp


def queue_actions(actions: list[str]) -> tp.List[str]:
    queue = []
    head = 0
    deleted_elements = []
    for a in actions:
        if a == "-":
            deleted_elements += [queue[head]]
            head += 1
        else:
            elem = a[2:]
            queue += [elem]
    return deleted_elements



def limits(actions_count: int, actions: tp.List[str]) -> bool:
    if (1 <= actions_count <= 10**6) and (len(actions) == actions_count):
        return True
    else:
        return False


def queue_actions_txt():
    f = File(__file__)
    arguments = f.read()
    actions_count = int(arguments[0])
    actions = arguments[1:]
    if limits(actions_count, actions):
        res = queue_actions(actions)
        f.write('\n'.join(res))



if __name__ == "__main__":
    queue_actions_txt()