# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите степень: "))
for i in range(num):
    degree = 2**i
    print(degree)