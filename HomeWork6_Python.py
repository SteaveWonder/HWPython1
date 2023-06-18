# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)

# a1 = int(input('Input a1 '))
# a = [0]*a1
# a[0] = int(input('Input a[0] '))
# d = int(input('Input d '))
# print(a[0], end=' ')
# for i in range(1, a1):
#     a[i]= a[i-1] + d
#     print(a[i], end = ' ')

# a1 = 7
# d = 2
# n = 5
# for i in range(n):
#     print(a1 + i * d, end=' ')    


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

"""
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end = ' ')
"""
"""
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 10
min = -2
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')
"""                