import math
from random import randint, shuffle
from multiprocessing import Pool
from functools import partial


def get_input_data():
    """
    Начальные данные
    """
    N = 40000
    win = 3
    return N, win


def one_iteration(x, win, n, N):
    x = set()
    while len(x) < n:
        m = randint(0, N)
        if m < win:
            return True
        x.add(m)
    return False


def do_iterations(N, win, n, count_iterations):
    with Pool(processes=12) as pool:
        one_iteration_partial = partial(one_iteration, win=win, n=n, N=N)
        results = pool.map(one_iteration_partial, range(count_iterations))
    return results


def main():
    """
    Основной цикл, запускающий одну итерацию несколько раз
    """
    N, win = get_input_data()
    count_iterations = 100_000
    n = 1000
    event_counter = sum(do_iterations(N, win, n, count_iterations))
    print(event_counter, count_iterations)
    print(f'Количество билетов: {N}, количество победных: {win}\n'
          f'Количество покупок с выигрышным билетом: {event_counter}\n'
          f'Количество покупок без выигрышного билета: {count_iterations - event_counter}\n'
          f'Смоделированная вероятность получения билета: {event_counter / count_iterations}\n'
          f'Расчетная вероятность получения билета: {1 - math.comb(N - win, n) / math.comb(N, n)}')


if __name__ == '__main__':
    main()
