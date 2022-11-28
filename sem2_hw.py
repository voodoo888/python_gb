"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

0,56 -> 11
"""
from math import factorial as fact


def sum_of_numbers(num):
    sum = 0
    for i in str(num):
        if i.isdigit():
            sum += int(i)
    print(sum)


sum_of_numbers(0.56)

"""
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def list_of_fact(num):
    result = []
    for i in range(1, num + 1):
        result.append(fact(i))
    return result


print(list_of_fact(5))

"""
3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

Пример:

Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
"""


def sum_of_numbers(num):
    result = []
    for i in range(1, num + 1):
        i = round(((1 + 1 / i) ** i), 2)
        result.append(i)
    print(sum(result))

sum_of_numbers(4)

"""
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
--> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0
"""
def create_list(num):
    result = []
    for i in range(-num, num + 1):
        result.append(i)
    return result

numbers4 = create_list(3)
print(numbers4)

indexes = input("ВВедите индексы одной строкой через пробел: ")
list_of_ind = indexes.split(" ")

result_sum = 1
for i in range(len(list_of_ind)):
    index = int(list_of_ind[i])
    result_sum *= numbers4[index]

print(result_sum)

"""
Реализуйте алгоритм перемешивания списка.
"""



# var1
list_of_values = [123, 24, "index", 13, "4", 51, 2, "asd"]

import random 
random.shuffle(list_of_values)
print(list_of_values)

# var2
list_of_values = [123, 24, "index", 13, "4", 51, 2, "asd"]

R_list = []
indexes_5 = []
for i in range(len(list_of_values)):
    indexes_5.append(i)

while len(list_of_values) > 0:
    index = indexes_5[random.randint(0, 7)]
    try:
        value = list_of_values.pop(index)
        R_list.insert(i, value)
    except IndexError:
        continue

print(R_list)
