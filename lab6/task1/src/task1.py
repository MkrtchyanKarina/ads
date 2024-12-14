import typing as tp
from lab6.src.utils import File

from llist import sllist


class HashTable:
    def __init__(self, array):
        self.table = {}
        self.answer = []
        self.array = array

    def add_key(self, key):
        h = hash(key)
        if h in self.table.keys():
            self.table[h].append(key)
        else:
            self.table[h] = sllist(key)

    def delete_key(self, key):
        h = hash(key)
        if h in self.table.keys():
            self.table.pop(h)
        else:
            pass

    def check_key(self, key):
        h = hash(key)
        if h in self.table.keys() and key in self.table[h]:
            self.answer += ['Y']
        else:
            self.answer += ['N']

    def actions(self):
        for a in self.array:
            command, key = a.split(" ")
            if command == "A":
                self.add_key(key)
            elif command == "D":
                self.delete_key(key)
            elif command == "?":
                self.check_key(key)
            else:
                pass
        return self.answer


def limits(length: int, commands: tp.List[str]) -> bool:
    if 1 <= length == len(commands) <= 5*10**5 and all(abs(int(x.split(" ")[1])) <= 10**18 for x in commands):
        return True
    else:
        return False


def hash_table_txt():
    f = File(__file__)
    arguments = f.read()
    length = int(arguments[0])
    commands = arguments[1:length+1]
    if limits(length, commands):
        ex = HashTable(commands).actions()
        answer = "\n".join(ex)
        f.write(answer)


if __name__ == "__main__":
    hash_table_txt()
