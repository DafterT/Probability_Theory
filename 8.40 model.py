import random
import numpy as np
import matplotlib.pyplot as plt
from math import log


def get_input_data():
    count_black = 2
    count_white = 20
    return count_white, count_black


def get_one_black_ball(count_black, count_white):
    return random.randint(1, count_black + count_white) <= count_black


def main():
    count_white, count_black = get_input_data()
    try_to_get = 1_000_000
    max_n = 200
    count_black_mas = np.zeros(max_n)
    n_now = 1
    count_iterations = 0
    for i in range(try_to_get):
        if get_one_black_ball(count_black, count_white):
            count_black_mas[n_now - 1] += 1
            count_iterations += 1
            n_now = 0
        n_now += 1
    chance = count_black_mas
    for i in range(1, max_n):
        chance[i] += chance[i - 1]
    chance = chance / count_iterations
    formula = [log(1 - i / 100) / log(1 - count_black / (count_white + count_black)) for i in range(0, 100)]
    plt.plot(range(1, max_n + 1), chance, label='model', linestyle='--', color='g', marker='o', markersize=3)
    plt.plot(formula, [i / 100 for i in range(0, 100)], label='formula', linestyle='--', color='r', marker='o',
             markersize=3)
    plt.legend()
    plt.savefig(f"pictures/8.40.Chance.jpg")
    plt.show()


if __name__ == '__main__':
    main()
