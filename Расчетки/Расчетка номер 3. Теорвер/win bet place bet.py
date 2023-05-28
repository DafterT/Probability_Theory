from game import *
import matplotlib.pyplot as plt


def round():
    destiny = random.randint(1, 6)
    while True:
        single_roll = roll()
        if destiny == 1:
            if single_roll == 4:
                return 1

        if destiny == 2:
            if single_roll == 5:
                return 2
        if destiny == 3:
            if single_roll == 6:
                return 3

        if single_roll == 7:
            return -1

        if destiny == 4:
            if single_roll == 8:
                return 3

        if destiny == 5:
            if single_roll == 9:
                return 2

        if destiny == 6:
            if single_roll == 10:
                return 1


def game(experiment):
    bet = 6
    win = 0
    game_outcomes = [0, 0, 0, 0]
    capital = bet
    game_number = 0
    game_length = 0
    overall_length = 0
    average_winnings = []
    round_history = []
    winnings = 0
    for i in range(1, experiment + 1):
        game_length += 1
        if capital <= 0:
            game_number += 1
            capital = bet
            overall_length += game_length
            game_length = 0
        lets_play = round()

        if lets_play == 1:
            game_outcomes[0] += 1
            round_history.append(1.8 * bet)
            win += 1
            winnings += 1.8 * bet
            capital += 1.8 * bet

        if lets_play == -1:
            game_outcomes[3] += 1
            round_history.append(-1 * bet)
            winnings -= bet
            capital -= bet

        if lets_play == 2:
            game_outcomes[1] += 1
            round_history.append(1.4 * bet)
            win += 1
            winnings += 1.4 * bet
            capital += 1.4 * bet

        if lets_play == 3:
            game_outcomes[2] += 1
            round_history.append(7)
            win += 1
            winnings += 7
            capital += 7
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
    x_values = ["4,10", "5,9", "6,8", "lose"]
    plt.vlines(x_values, 0, probabilities)
    plt.show()


if __name__ == '__main__':
    main()
