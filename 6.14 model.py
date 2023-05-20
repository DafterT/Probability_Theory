import random


def get_input_data():
    box = [1] * 9 + [0] * 6
    count_to_taken = 3
    return box, count_to_taken


def simulate_game(box, count_to_taken):
    random.shuffle(box)
    first_game = random.sample(box, count_to_taken)  # выбираем 3 мяча для первой игры
    for ball in first_game:
        box.remove(ball)  # удаляем выбранные мячи из ящика
    box.extend([0] * count_to_taken)
    second_game = random.sample(box, count_to_taken)  # выбираем 3 мяча для второй игры
    return all(ball == 1 for ball in second_game)  # проверяем, все ли мячи новые


def main():
    box, count_to_taken = get_input_data()
    num_experiments = 1000000  # количество экспериментов
    num_successes = 0  # количество успешных экспериментов

    for _ in range(num_experiments):
        if simulate_game(box.copy(), count_to_taken):
            num_successes += 1

    probability = num_successes / num_experiments
    print(f'Вероятность того, что все мячи для второй игры будут новыми: {probability}\n'
          f'Теоретическая вероятность: 0.089 для коробки 9 новых мячей и 6 старых')


if __name__ == '__main__':
    main()
