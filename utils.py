import pathlib

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1

class File:
    def __init__(self, file):
        self.file = file.split('\\')
        self.task_number = self.file[-1][4:-3]
        self.lab_folder = self.file[5]
        self.task_folder = f'task{self.task_number}'


    def read(self):
        input_file = f'input{self.task_number}.txt'
        path = pathlib.Path(pathlib.Path(__file__).parent, self.lab_folder, self.task_folder, 'txtf', input_file)
        file = open(path, 'r', encoding="utf-8")
        arguments = file.read().split("\n")
        return arguments

    def write(self, result: str):
        output_file = f'output{self.task_number}.txt'
        path = pathlib.Path(pathlib.Path(__file__).parent, self.lab_folder, self.task_folder, 'txtf', output_file)
        file = open(path, 'w', encoding="utf-8")
        file.write(result)