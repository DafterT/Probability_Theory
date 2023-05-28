import math
import random
import numpy as np


def get_input_data():
    h = 5
    l = 10
    return h, l


def one_iteration(h, l):
    ab = random.uniform(0, l)
    angle = math.atan(ab / h)
    return angle


def main():
    h, l = get_input_data()
    count_iterations = 1_000_000
    angels = []
    for _ in range(count_iterations):
        angels.append(one_iteration(h, l))
    print(f'Полученное математическое ожидание: {np.mean(angels)}\n'
          f'Теоретическое математическое ожидание: {math.atan(l / h) - h / (2 * l) * math.log(1 + l ** 2 / h ** 2)}')


if __name__ == '__main__':
    main()
