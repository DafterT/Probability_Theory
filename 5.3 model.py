from random import random, randint

import numpy as np


def get_input_data():
    # Размерность массива
    n = 10
    return n


def generate_array(n):
    """
    Создает массив случайных чисел, сумма которых равна 1, размерности n на n
    """
    random_nums = np.random.rand(n, n)
    total_sum = np.sum(random_nums)
    result_array = random_nums / total_sum
    return result_array


def main():
    n = get_input_data()
    P = generate_array(n)
    k = randint(0, n - 1)
    count_in_k = 0
    count_iterations = 1000000
    for i in range(count_iterations):
        chance = random()
        sum_chance = 0
        counter = 0
        while chance > sum_chance:
            sum_chance += P[counter // n][counter % n]
            counter += 1
        if (counter - 1) // n == k:
            count_in_k += 1
    print(f'Теоретическая вероятность: {np.sum(P[k, :])}\n'
          f'Полученная вероятность: {count_in_k / count_iterations}')


if __name__ == '__main__':
    main()
