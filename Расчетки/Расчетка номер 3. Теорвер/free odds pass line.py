from game import *
import matplotlib.pyplot as plt


def round():
    point = roll()
    if point in (7, 11):
        return 'dp'
    if point in (2, 3, 12):
        return 0
    while True:
        roll_result = roll()
        if roll_result == point:
            return point
        if roll_result == 7:
            return 2


def game(experiment):
    bet = 1
    win = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    round_history = []
    average_winnings = []
    game_outcomes = [0, 0, 0, 0, 0, 0]

    winnings = 0
    for i in range(1, experiment + 1):
        game_length += 1
        if capital <= 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()

        if lets_play == 'dp':
            game_outcomes[0] += 1
            round_history.append(bet)
            win += 1
            winnings += bet
            capital += bet

        if lets_play in (4, 10):  # сделали 4 10
            game_outcomes[1] += 1
            round_history.append(bet * 2 + bet)
            win += 1
            winnings += bet * 2 + bet
            capital += bet * 2 + bet

        if lets_play in (5, 9):  # сделали 5 9
            game_outcomes[2] += 1
            round_history.append(bet * 1.5 + bet)
            win += 1
            winnings += bet * 1.5 + bet
            capital += bet * 1.5 + bet

        if lets_play in (6, 8):  # сделали 6 8
            game_outcomes[3] += 1
            round_history.append(bet * 1.2 + bet)
            win += 1
            winnings += bet * 1.2 + bet
            capital += bet * 1.2 + bet

        if lets_play == 2:  # для фри одс
            game_outcomes[4] += 1
            round_history.append(-bet * 2)
            winnings -= bet * 2
            capital -= bet * 2

        if lets_play == 0:  # для пас лайна
            game_outcomes[5] += 1
            round_history.append(-bet)
            winnings -= bet
            capital -= bet

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
    x_values = ["x2", "x3", "x2.5", "x2.2", "lose_all", "lose_pass"]
    plt.vlines(x_values, 0, probabilities)
    plt.show()


if __name__ == '__main__':
    main()
