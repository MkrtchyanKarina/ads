import os
import pathlib
import subprocess
import sys
sys.path.append('C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures')
project_path = pathlib.Path(__file__).parent.parent
array = os.listdir(project_path)
src_path = []

for i in range(2, 9): # в цикле от первой до последней папки
    task = array[i]

    dir_path = pathlib.Path(project_path, task) # получаем директорию index-ой папки
    src_path += [pathlib.Path(dir_path, "src", f'{task}.py')]


if __name__ == "__main__":
    for f in src_path:
        subprocess.run(['python', str(f)])
        print(f'{f}  ran')