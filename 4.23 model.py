import math
from random import randint
from multiprocessing import Pool
from functools import partial
import matplotlib.pyplot as plt


def get_input_data():
    """
    Начальные данные
    """
    N = 40000
    win = 3
    return N, win


def one_iteration(x, win, n, N):
    """
    Одна покупка n билетов
    """
    x = set()
    while len(x) < n:
        m = randint(0, N)
        if m < win:
            return True
        x.add(m)
    return False


def do_iterations(N, win, n, count_iterations):
    """
    Функция для выполнения нескольких покупок
    """
    with Pool(processes=8) as pool:
        one_iteration_partial = partial(one_iteration, win=win, n=n, N=N)
        results = pool.map(one_iteration_partial, range(count_iterations))
    return results


def main():
    N, win = get_input_data()
    # Решение пункта a
    count_iterations = 10_000
    n = 1000
    event_counter = sum(do_iterations(N, win, n, count_iterations))
    print(f'Пункт a:'
          f'Количество билетов: {N}, количество победных: {win}\n'
          f'Количество покупок с выигрышным билетом: {event_counter}\n'
          f'Количество покупок без выигрышного билета: {count_iterations - event_counter}\n'
          f'Смоделированная вероятность получения билета: {event_counter / count_iterations}\n'
          f'Расчетная вероятность получения билета: {1 - math.comb(N - win, n) / math.comb(N, n)}')
    # Пункт b
    count_iterations = 100
    chance = []
    real_chance = []
    points = list(range(1000, 20000, 500))
    for n in points:
        event_counter = sum(do_iterations(N, win, n, count_iterations))
        chance.append(event_counter / count_iterations)
        real_chance.append(1 - math.comb(N - win, n) / math.comb(N, n))
    plt.plot(points, chance, label='Model', linestyle='--', color='r', marker='o', markersize=3)
    plt.plot(points, real_chance, label='Real', linestyle='--', color='g', marker='o', markersize=3)
    plt.savefig(f"Chance.jpg")
    plt.show()


if __name__ == '__main__':
    main()
