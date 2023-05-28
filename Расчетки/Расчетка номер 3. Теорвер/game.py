import collections
import math
import random
import statistics

import numpy as np
from matplotlib import pyplot as plt


def roll():
    """
    Генерирует два случайных числа,
    имитирующих бросок кубиков и возвращает их сумму
    """
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1 + dice_2


def roll_double():
    """
    Генерирует два случайных числа,
    имитирующих бросок кубиков и возвращает их сумму
    и информацию, дабл ли это
    """
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1 + dice_2, dice_2 == dice_1


def building_confidence_probability(round_history, average_winnings):
    """
    Функция для постройки доверительной вероятности
    """
    list_intervals_down = []
    list_intervals_up = []
    dispersion = np.var(round_history)
    for i in range(0, len(round_history) - 1):
        list_intervals_down.append(average_winnings[i + 1] - (1.65 / math.sqrt(i + 1)) * dispersion)
        list_intervals_up.append(average_winnings[i + 1] + (1.65 / math.sqrt(i + 1)) * dispersion)
    return list_intervals_down, list_intervals_up


def print_confidence_probability(list_intervals_down, list_intervals_up):
    """
    Функция для отрисовки доверительной вероятности
    """
    plt.title("График доверительной вероятности")
    plt.plot(list_intervals_down)
    plt.plot(list_intervals_up)
    plt.show()


def print_average_winnings(average_winnings, experiment):
    """
    Функция для отрисовки средних выигрышей
    """
    plt.title("График средних выигрышей")
    plt.plot(average_winnings)
    plt.hlines(np.median(average_winnings), 0, experiment, colors='r', label='Медиана')
    a = np.std(average_winnings)
    plt.hlines(a, 0, experiment, colors='g', label='СКО')
    plt.hlines(-a, 0, experiment, colors='y', label='-СКО')
    plt.ylim(-0.2, 0.2)
    plt.xlim(0, 10000)
    plt.legend()
    plt.show()


def print_distribution_winnings(round_history, experiment, situations):
    """
    Функция для отрисовки распределения выигрышей
    """
    plt.title("График распределения выигрышей")
    for i in situations:
        plt.vlines(i, 0, round_history.count(i) / experiment)
    plt.show()


def print_results(win, experiment, winnings, bet, overall_length, game_number, round_history):
    print(f'Шанс победы: {win / experiment}\n'
          f'Ожидаемый выигрыш: {winnings}')

    EV_per_Unit = winnings / (experiment * bet)
    print(f'Ожидаемый выигрыш за 1 ставку: {EV_per_Unit}\n'
          f'Доход заведения: {EV_per_Unit * 100}')

    return_to_player = 1 + winnings / (experiment * bet)
    print(f'Процент возврата игроку: {return_to_player}')

    counts = collections.Counter(round_history)
    var = 0
    for el, count in counts.items():
        var += (el - EV_per_Unit) ** 2 * (count / experiment)
    print(f'Дисперсия: {var}')

    standard_deviation = var ** 0.5
    print(f'Среднеквадратичное отклонение: {standard_deviation}')

    print(f'Средний суммарный выигрыш: {EV_per_Unit * experiment}\n'
          f'Среднее квадратическое отклонение: {standard_deviation * (experiment ** 0.5)}')

    VI = 1.65 * standard_deviation
    confidence_interval_low = return_to_player - VI / math.sqrt(experiment)
    confidence_interval_up = return_to_player + VI / math.sqrt(experiment)

    print(f'Доверительный интервал: [{confidence_interval_low}; {confidence_interval_up}]\n'
          f'Индекс волатильности игры: {VI}\n'
          f'Средняя продолжительность игры: {overall_length / game_number}')


def build_graphic(list_intervals_down, list_intervals_up, average_winnings, experiment, round_history, situations):
    print_confidence_probability(list_intervals_down, list_intervals_up)
    print_average_winnings(average_winnings, experiment)
    print_distribution_winnings(round_history, experiment, situations)
