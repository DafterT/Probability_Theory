from game import *
import matplotlib.pyplot as plt


def round():
    point = roll()
    if point in (7, 11):
        return -1
    if point in (2, 3):
        return 0
    if point == 12:
        return
    while True:
        roll_result = roll()
        if roll_result == point:
            return 2
        if roll_result == 7:
            return point


def game(experiment):
    bet = 1
    win = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    average_winnings = []
    round_history = []
    game_outcomes = [0, 0, 0, 0, 0, 0, 0]

    winnings = 0
    for i in range(1, experiment + 1):
        game_length += 1
        if capital <= 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play == -1:
            game_outcomes[0] += 1
            round_history.append(-bet)
            winnings -= bet
            capital -= bet
        if lets_play == 2:
            game_outcomes[1] += 1
            round_history.append(-bet * 2)
            winnings -= bet * 2
            capital -= bet * 2
        if lets_play == 0:
            game_outcomes[2] += 1
            round_history.append(bet)
            win += 1
            winnings += bet
            capital += bet
        if lets_play in (4, 10):
            game_outcomes[3] += 1
            round_history.append(bet * 0.5 + bet)
            win += 1
            winnings += bet * 0.5 + bet
            capital += bet * 0.5 + bet
        if lets_play in (5, 9):
            game_outcomes[4] += 1
            round_history.append(bet * 0.66 + bet)
            win += 1
            winnings += bet * 0.66 + bet
            capital += bet * 0.66 + bet
        if lets_play in (6, 8):
            game_outcomes[5] += 1
            round_history.append(bet * 0.83 + bet)
            win += 1
            winnings += bet * 0.83 + bet
            capital += bet * 0.83 + bet
        if lets_play is None:
            round_history.append(0)
            game_outcomes[6] += 1
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
    x_values = ["lose_pass", "lose_point", "win_dont_pass", "win4_10", "win5_9", "win6_8", "bet_return"]
    plt.xticks(rotation=-15)
    plt.vlines(x_values, 0, probabilities)
    plt.show()


if __name__ == '__main__':
    main()
