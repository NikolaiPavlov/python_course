# Задача 32
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list = [ int(x) for x in input( 'Задайте массив'
                                '(через пробел): ' ).split() ]
a = int(input('Введите диапазон:\nот '))
b = int(input('до '))
result = []
if a > b:
    print('Ошибка')
else:
    for i in range(len(list)):
        if list[i] >= a and list[i] <= b:
            result.append(i)
print(*result)