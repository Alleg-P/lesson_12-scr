# Задача 3: Использование лямбда-функций для фильтрации данных

data_sets = [
    ([10, 23, 35, 47], lambda x: x % 2 != 0),

    ([5, 7, 8, 10], lambda x: x > 7),

    ([1, 2, 3, 5, 6], lambda x: x < 5),

    ([10, 20, 30, 40, 50], lambda x: x % 5 == 0 and x % 8 == 0)
]

def filter_data(data, filter_func):
    return list(filter(filter_func, data))

for data, filter_func in data_sets:
    filtered_data = filter_data(data, filter_func)
    print("Отфильтрованные данные:", filtered_data)
