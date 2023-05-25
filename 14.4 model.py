import numpy as np
import matplotlib.pyplot as plt
import random


def get_input_data():
    max_deviation = 5
    norm_deviation = 2
    required_chance = 0.9
    return max_deviation, norm_deviation, required_chance


def do_one_iteration(max_deviation, norm_deviation):
    return abs(random.gauss(0, max_deviation)) <= norm_deviation


def do_iterations(max_deviation, norm_deviation, count_iterations):
    norm_detail = np.zeros(50)
    count = 0
    for _ in range(count_iterations):
        iteration = 1
        while not (do_one_iteration(max_deviation, norm_deviation)):
            iteration += 1
        if iteration <= 100:
            count += 1
            norm_detail[iteration] += 1
    return norm_detail / count


def main():
    max_deviation, norm_deviation, required_chance = get_input_data()
    count_iterations = 1_000_000
    chances = do_iterations(max_deviation, norm_deviation, count_iterations)
    printed = False
    for i in range(1, len(chances)):
        chances[i] += chances[i - 1]
        if chances[i] > required_chance and not printed:
            print(f'Функция достигла заданного значения вероятности {required_chance} на детали {i}')
            printed = True
    plt.plot([i for i in range(len(chances))], chances, color='r', linewidth=2)
    plt.grid()
    plt.savefig("pictures/14.4.Chance.jpg")
    plt.show()


if __name__ == '__main__':
    main()
