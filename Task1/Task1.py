# Задача 1
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input('Введите сколько километров за день проезжает машина: '))
m = int(input('Введите сколько нужно проехать километров: '))

print((m+n-1)//n)