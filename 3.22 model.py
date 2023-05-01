import math
from random import random


def get_input_data():
    """
    Начальные данные
    """
    l = 3
    L = 7
    return l, L


def get_random_x_fi(L):
    """
    Получение результата броска иголки
    """
    x = random() * L / 2
    fi = random() * math.pi
    return x, fi


def one_iteration(L, l):
    """
    Одна итерация
    """
    x, fi = get_random_x_fi(L)
    return l * math.sin(fi) / 2 > x


def main():
    """
    Основной цикл, запускающий одну итерацию несколько раз
    """
    l, L = get_input_data()
    event_counter = 0
    count_iterations = 1_000_000
    for i in range(0, count_iterations):
        iteration = one_iteration(L, l)
        event_counter += iteration
    print(f'Расстояние между прямыми: {L}, длина прямой: {l}\n'
          f'Количество падений иглы на прямую: {event_counter}\n'
          f'Количество падений иглы мимо прямой: {count_iterations - event_counter}\n'
          f'Смоделированная вероятность падения иглы на прямую: {event_counter / count_iterations}\n'
          f'Расчетная вероятность падения иглы на прямую: {2 * l / (math.pi * L)}')


if __name__ == '__main__':
    main()
