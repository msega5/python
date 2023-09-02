# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной
# и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import random


tails, eagle = 0, 0
coin = int(input("Введите количество монет: "))
for i in range(coin):
    coin_side = random.randint(0, 1)
    if coin_side == 0:
        tails += 1
    else:
        eagle += 1
    i += 1
if tails > eagle:
    print(f"Орлов меньше, их {eagle} из {coin}")
elif tails < eagle:
    print(f"Решек меньше, их {tails} из {coin}")
else:
    print(f"Решек и орлов поровну по {eagle}")
