# Задача 1: Цепочка функций обработки данных

import statistics

data1 = [1, 2, 3, 4, 5]
data2 = [10, 15, 5, 20]

def collect_data(data):
    return process_data(data)

def process_data(data):
    average = statistics.mean(data)
    return summarize_data(average)

def summarize_data(average):
    return print(f"Итог: Среднее значение: {average}")

collect_data(data1)
collect_data(data2)
