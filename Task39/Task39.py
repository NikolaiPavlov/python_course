# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# (каждое число вводится с новой строки)


import random
n = int(input('Введите количество элементов первого массива: '))
first = []
for i in range(n):
    first.append(random.randint(1, 10))
m = int(input('Введите количество элементов второго массива: '))
second = []
for i in range(m):
    second.append(random.randint(1, 10))
print(first)
print(second)

count = 0
for i in range(n):
    for j in range(m):
        if first[i] == second[j]:
            count += 1
    if count == 0:
        print(first[i], end=' ')
    count = 0
print('\n')