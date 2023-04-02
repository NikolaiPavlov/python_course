a = int(input('Число 1:'))
b = int(input('Число 2:'))

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

print(sum(a, b))