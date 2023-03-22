# Задача №11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

fibo = [0, 1]
i = 0
j = 1
index = 2

num = int(input("Введите число: "))

while j < num:
    next_el = i + j
    fibo.append(next_el)
    i = j
    j = next_el
    index += 1
print(fibo)

if j == num:
    print(index)
else:
    print(-1)