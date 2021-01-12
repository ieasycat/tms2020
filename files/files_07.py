"""
Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл
"""

from random import randint
import json


def create_matrix():
    matrix = []
    for i in range(3):
        tmp = []
        for k in range(3):
            tmp.append(randint(1, 9))
        matrix.append(tmp)
    with open('files_07', 'w') as my_file:
        data = json.dumps(matrix, indent=4)
        my_file.write(data)


def open_json(json_file):
    with open(json_file) as my_file:
        data = json.loads(my_file.read())
    return data


def reset(data):
    for i, row in enumerate(data):
        for j, elem in enumerate(row):
            if elem % 2 == 0:
                data[i][j] = None
    new_data = json.dumps(data, indent=4)
    return new_data


def new_json(data):
    with open('files_new_07', 'w') as new_file:
        new_file.write(data)


def main():
    file = 'files_07'
    create_matrix()
    new_open = open_json(file)
    new_res = reset(new_open)
    new_json(new_res)


if __name__ == '__main__':
    main()
