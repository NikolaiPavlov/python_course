# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

n = int(input())

A = []
i = 0
while i < n:
    A.append(random.randint(0, 10))
    i += 1
print(A)

x = int(input())

j = 0
result = 0
s = 11
while j < n:
    if s > abs(A[j] - x):
        result = A[j]
        s = abs(A[j] - x)
    j += 1
print(result)