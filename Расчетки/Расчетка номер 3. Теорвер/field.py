from game import *
import matplotlib.pyplot as plt


def round():
    field_point = roll()
    bet = 1
    while True:
        if field_point in (3, 4, 9, 10, 11):
            return bet
        if field_point in (2, 12):
            return bet * 2
        if field_point in (5, 6, 7, 8):
            return -bet


def game(experiment):
    bet = 1
    win = 0
    game_outcomes = [0, 0, 0]
    average_winnings = []
    round_history = []
    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0

    winnings = 0
    for i in range(1, experiment + 1):
        game_length += 1
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play == 1:
            game_outcomes[0] += 1
            round_history.append(1)
            win += 1
            winnings += bet
            capital += bet
        if lets_play == -1:
            game_outcomes[1] += 1
            round_history.append(-1)
            winnings -= bet
            capital -= bet
        if lets_play == 2:
            game_outcomes[2] += 1
            round_history.append(2)
            win += 1
            winnings += bet * 2
            capital += bet * 2
        average_winnings.append(winnings / (i * bet))
    list_intervals_down, list_intervals_up = building_confidence_probability(round_history, average_winnings)
    print_results(win, experiment, winnings, bet, overall_length, game_number, round_history)
    return list_intervals_down, list_intervals_up, average_winnings, round_history, game_outcomes


def main():
    experiment = 1_000_000
    list_intervals_down, list_intervals_up, average_winnings, round_history, game_outcomes = game(experiment)
    print_confidence_probability(list_intervals_down, list_intervals_up)
    print_average_winnings(average_winnings, experiment)
    # Вывод распределения выигрышей
    plt.title("График распределения выигрышей")
    probabilities = (list(map(lambda x: x / experiment, game_outcomes)))
    x_values = ["win", "loose", "win_x2"]
    plt.vlines(x_values, 0, probabilities)
    plt.show()


if __name__ == '__main__':
    main()
