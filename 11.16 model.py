import random
import numpy as np
from matplotlib import pyplot as plt


def get_input_data():
    n = 10  # Количество элементов типа A
    m = 5  # Количество элементов типа B
    return n, m


def simulate_failures(n, m, num_trials):
    count_failures = np.zeros(num_trials)
    for i in range(num_trials):
        a_elements = n
        b_elements = m
        while a_elements > 0:
            element = random.randint(1, a_elements + b_elements)
            if element <= a_elements:
                a_elements -= 1
            count_failures[i] += 1
        if i < num_trials - 1:
            count_failures[i + 1] = count_failures[i]
        count_failures[i] /= i + 1

    return count_failures


def main():
    # Параметры моделирования
    n, m = get_input_data()
    num_trials = 100_000  # Количество испытаний

    average_failures = simulate_failures(n, m, num_trials)
    real_answer = n + m * sum([1 / i for i in range(1, n + 1)])
    print(f'Среднее число отказов элементов: {average_failures[-1]}\n'
          f'Среднее число отказов в теории: {real_answer:.6}')
    plt.plot(range(num_trials), average_failures, label='model', color='g')
    plt.plot(range(num_trials), [real_answer for _ in range(num_trials)], label='formula', linestyle='--', color='r')
    plt.legend()
    plt.savefig("pictures/11.16.Chance.jpg")
    plt.show()


if __name__ == '__main__':
    main()
