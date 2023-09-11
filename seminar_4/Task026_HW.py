# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.

# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите размер массива 1 = '))
m = int(input('Введите размер массива 2 = '))
array_n, array_m = [], []

for i in range(0, n):
    rand_num = random.randint(0, 10)
    array_n.append(rand_num)

for i in range(0, m):
    rand_num = random.randint(0, 10)
    array_m.append(rand_num)

print(f'Начальные массивы: {array_n, array_m}')

array_u = sorted(set(array_n).union(set(array_m)))
print(f'Конечный массив: {array_u}')