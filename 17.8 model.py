import numpy as np


def get_input_data():
    k = 1
    a = 8
    b = 5
    return k, a, b


def in_ellipse(x, y, a, b):
    return x ** 2 / a ** 2 + y ** 2 / b ** 2 <= 1


# Отклонение, ожидание
def get_coordinate(std_dev, mean=0):
    return np.random.normal(mean, std_dev)


def main():
    k, a, b = get_input_data()
    count_iterations = 1_000_000
    in_ellipse_counter = 0
    for _ in range(count_iterations):
        x, y = get_coordinate(a), get_coordinate(b)
        if in_ellipse(x, y, a * k, b * k):
            in_ellipse_counter += 1
    print(f'Всего испытаний: {count_iterations}\n'
          f'В эллипсе оказалось: {in_ellipse_counter}\n'
          f'Итоговая вероятность: {in_ellipse_counter / count_iterations}\n'
          f'Теоретическая вероятность: {1 - np.e ** (-(k ** 2) / 2)}')


if __name__ == '__main__':
    main()
