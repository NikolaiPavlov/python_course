# Задача 24

n = int(input('Количество кустов: '))

list = [ int(x) for x in input( 'Введите '
                                'количество ягод '
                                'на каждом кусте '
                                '(через пробел): ' ).split() ]

n = len(list)

list = list + list[:2]

m = 0

for i in range(n):
    m = max( m, list[i] + list[i+1] + list[i+2] )
print(m)