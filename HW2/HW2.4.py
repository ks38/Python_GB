# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# это задание не понял вообще :(
# даже найдя решение в интернете

import random


def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2 * number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int, data.readlines()))
    return indexs
