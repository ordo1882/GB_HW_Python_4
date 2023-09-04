# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

n = int(input("Enter the bushes number: "))

bushes_list = [random.randint(10, 100) for i in range(n)]

print('Bushes list:',*bushes_list)

for i in range(len(bushes_list)):
    if i == 0:
        best_case = bushes_list[-1] + bushes_list[i] + bushes_list[i + 1]
        bush = i + 1 

    elif i == n - 1:
        berries_count = bushes_list[i - 1] + bushes_list[i] + bushes_list[0]
        if berries_count > best_case:
            best_case = berries_count
            bush = i + 1

    else:
        berries_count = bushes_list[i - 1] + bushes_list[i] + bushes_list[i + 1]
        if berries_count > best_case:
            best_case = berries_count
            bush = i + 1

print(f"Best case is {best_case} berries\nSource bush №{bush}")