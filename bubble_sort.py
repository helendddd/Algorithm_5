#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time


def bubble_sorting(arr):
    for i in range((len(arr)) - 1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    array_lengths = list(range(100, 1100, 100))

    for length in array_lengths:
        array_to_sort = list(range(length))

        # Худший случай
        array_to_sort.reverse()
        start_time_worst = time.time()
        bubble_sorting(array_to_sort)
        end_time_worst = time.time()
        exe_time_worst = end_time_worst - start_time_worst

        # Средний случай
        random.shuffle(array_to_sort)
        start_time_average = time.time()
        bubble_sorting(array_to_sort)
        end_time_average = time.time()
        exe_time_average = end_time_average - start_time_average

        print(f"Время выполнения худшего случая: {exe_time_worst} сек.")
        print(f"Время выполнения среднего случая: {exe_time_average} сек.\n")
