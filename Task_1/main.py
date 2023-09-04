# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

n = int(input("Enter first list lenght: "))
m = int(input("Enter second list lenght: "))

list_1 = [random.randint(0, 15) for i in range(n)]
list_2 = [random.randint(0, 15) for i in range(m)]

set_1 = set(list_1)
set_2 = set(list_2)

common_numbers = set_1.intersection(set_2)

sorted_common_numbers = list(common_numbers)

sorted_common_numbers.sort()

print("First list:", *list_1)
print("Second list:", *list_2)
print("Common numbers:", *sorted_common_numbers)