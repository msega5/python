# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное
# число ягод — на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

bush_count = random.randint(3, 22) 
bed, max_num, temp, array_max = [], 0, 0, []
for i in range(bush_count):
    berries = random.randint(1, 100)
    bed.append(berries)
print(bed)

for i in range(len(bed)):    
    max_num = bed[0] + bed[1] + bed[2]
    array_max.append(max_num)
    temp = bed.pop()
    bed.insert(0, temp)

print(sorted(array_max))
print(f'Максимальное число ягод с кустов за один заход = {max(array_max)}')