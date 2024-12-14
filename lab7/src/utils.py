import pathlib

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class File:
    def __init__(self, file):
        self.file = file
        self.task_number = self.file.split('\\')[-1][4:-3]
        self.folder = f'task{self.task_number}'

    def read(self):
        input_file = f'input{self.task_number}.txt'
        path = pathlib.Path(pathlib.Path(__file__).parent.parent, self.folder, 'txtf', input_file)
        file = open(path, 'r', encoding="utf-8")
        arguments = file.read().split("\n")
        return arguments

    def write(self, result: str):
        output_file = f'output{self.task_number}.txt'
        path = pathlib.Path(pathlib.Path(__file__).parent.parent, self.folder, 'txtf', output_file)
        file = open(path, 'w', encoding="utf-8")
        file.write(result)