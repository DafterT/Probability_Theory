from random import randint


def get_input_data():
    count_20 = 3
    count_3 = 7
    return count_20, count_3


def get_random_coin(count_20, count_3):
    """
    Получение результата доставания монетки
    """
    x = randint(1, count_3 + count_20)
    if x <= count_20:
        return 20
    return 3


def one_iteration(count_20, count_3):
    """
    Одна итерация вытягивания двух монет
    """
    first_coin = get_random_coin(count_20, count_3)
    if first_coin == 20:
        count_20 -= 1
    else:
        count_3 -= 1
    second_coin = get_random_coin(count_20, count_3)
    if second_coin != 20:
        return
    return 1 if first_coin == 20 else 0


def main():
    """
    Основной цикл, запускающий одну итерацию несколько раз
    """
    count_20, count_3 = get_input_data()
    iteration_counter = 0
    event_counter = 0
    while iteration_counter < 1_000_000:
        iteration = one_iteration(count_20, count_3)
        if iteration is None:
            continue
        event_counter += iteration
        iteration_counter += 1
    print(f'Количество 20-ок: {count_20}, количество 3-ек: {count_3}\n'
          f'Количество попыток, когда второй раз выпала 20: {iteration_counter}\n'
          f'Количество выпадений двух 20 подряд: {event_counter}\n'
          f'Итоговая вероятность: {event_counter / iteration_counter}\n'
          f'Ожидаемая вероятность: {(count_20 - 1) / (count_20 + count_3 - 1)}')


if __name__ == '__main__':
    main()
