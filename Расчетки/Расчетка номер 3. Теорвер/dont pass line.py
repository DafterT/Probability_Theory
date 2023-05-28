from game import *


def round():
    point = roll()
    if point in (7, 11):
        return -1
    elif point in (2, 3):
        return 1
    elif point == 12:
        return 0
    while True:
        roll_result = roll()
        if roll_result == point:
            return -1
        elif roll_result == 7:
            return 1


def game(experiment):
    bet = 1
    win = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    round_history = []
    average_winnings = []

    winnings = 0
    for i in range(experiment):
        game_length += 1
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play == 0:
            round_history.append(0)
        elif lets_play == -1:
            round_history.append(-1)
            winnings -= bet
            capital -= bet
        elif lets_play == 1:
            round_history.append(1)
            win += 1
            winnings += bet
            capital += bet
        average_winnings.append(winnings / ((i + 1) * bet))

    # Построение дов. вероятности
    list_intervals_down, list_intervals_up = building_confidence_probability(round_history, average_winnings)
    # Вывод результатов
    print_results(win, experiment, winnings, bet, overall_length, game_number, round_history)
    return list_intervals_down, list_intervals_up, average_winnings, round_history


def main():
    experiment = 1_000_000
    list_intervals_down, list_intervals_up, average_winnings, round_history = game(experiment)
    build_graphic(list_intervals_down, list_intervals_up, average_winnings, experiment, round_history, (-1, 0, 1))


if __name__ == '__main__':
    main()
