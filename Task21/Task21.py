# Задача №21
# Напишите программу для печати всех уникальных
# значений в словаре.

source = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005 "},
    {"V": "S009"},
    {"VIII": "S007"}
]


def unic_printer(list_data):
    result = set()
    for item in list_data:
        result.add(*item.values())
    print(result)


unic_printer(source)