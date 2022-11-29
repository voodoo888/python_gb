"""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

Пример:

[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
"""
A = [2, 3, 5, 9, 3]


def sum_of_not_even_ind(list_):
    sum = 0
    for i in range(len(list_)):
        if i % 2 != 0:
            sum += list_[i]
    return sum


print(sum_of_not_even_ind(A))


"""
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
A = [2, 3, 4, 5, 6]
B = [2, 3, 5, 6]


def pairs_of_product(list_):
    result = []
    for i in range((len(list_) + 1) // 2):
        result.append(list_[i] * list_[len(list_) - i - 1])
    return result


print(pairs_of_product(A))
print(pairs_of_product(B))

"""
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 10.01] => 0.19
"""

A = [1.1, 1.2, 3.1, 10.01]
temp_list = []

for i in A:
    temp_list.append(i - round(i))

result = round((max(temp_list) - min(temp_list)), 3)
print(result)

"""
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def ToBinar(n):
    result = []
    while n > 0:
        result.append(n % 2)
        n = n // 2
    result = result[::-1]

    print("".join(map(str, result)))

ToBinar(45)
ToBinar(3)
ToBinar(2)

"""
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""
# def fiba_minus(n):
#     # # len_of_list = n * 2 + 1
#     # temp_list = []
#     # for i in range(0, -n - 1, -1):
#         if i == 0:
#             temp_list.append(0)
#         if i == -1:
#             temp_list.append(1)
#         if i == -2:
#             temp_list.append(-1)
#         else:
#             temp_list.append(fiba_minus(n + 2) - fiba_minus(n + 1))


# fiba_minus(8)

def fiba(n):
    if n in (1, 2):
        return 1
    return fiba(n - 1) + fiba(n - 2)

def fiba_minus(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return fiba_minus(n +2) - fiba_minus(n + 1)

# print(fiba_minus(-6))

def fibalist(n):
    fiba_list = []
    
    for i in range((-n), 0):
        fiba_list.append(fiba_minus(i))

    fiba_list.append(0)

    for i in range(1, n + 1):
        fiba_list.append(fiba(i))

    print(fiba_list)

fibalist(8)


