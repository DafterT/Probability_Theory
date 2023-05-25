import random
import math
import matplotlib.pyplot as plt
import numpy as np


def get_input_data():
    v0 = 50
    g = 9.8
    return v0, g


def do_one_iteration(v0, g):
    angle = random.uniform(0, math.pi / 2)
    return v0 ** 2 * math.sin(2 * angle) / g


def do_iterations(v0, g, count_iterations):
    distances = [do_one_iteration(v0, g) for _ in range(count_iterations)]
    return sorted(distances)


def main():
    v0, g = get_input_data()
    count_iterations = 1_000_000
    distances = do_iterations(v0, g, count_iterations)
    # График
    plt.hist(distances, bins='auto', density=True, cumulative=True, alpha=0.7)
    x = np.sort(distances)
    y = np.arange(1, len(x) + 1) / len(x)
    plt.plot(x, y, color='r', linewidth=3)
    # Теоретический результат
    x = np.linspace(min(x), max(x), 100)
    y = 2 / np.pi * np.arcsin(x * g / (v0 ** 2))
    plt.plot(x, y, color='g', linewidth=2)
    plt.savefig("pictures/12.17.Chance.jpg")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
