from game import *
import matplotlib.pyplot as plt


def round():
    single_roll = roll()
    if single_roll in (2, 12, 3, 11):
        return single_roll
    return -1


def game(experiment):
    bet = 1
    win = 0
    average_winnings = []
    round_history = []
    game_outcomes = [0, 0, 0, 0, 0]
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
        destiny = random.randint(1, 4)
        if lets_play == 2:
            if destiny == 1:
                game_outcomes[1] += 1
                round_history.append(bet * 6.75 * 2)
                win += 1
                winnings += bet * 6.75 * 2
                capital += bet * 6.75 * 2
            else:
                game_outcomes[0] += 1
                round_history.append(bet * 6.75)
                win += 1
                winnings += bet * 6.75
                capital += bet * 6.75

        if lets_play == 12:
            if destiny == 2:
                game_outcomes[1] += 1
                round_history.append(bet * 6.75 * 2)
                win += 1
                winnings += bet * 6.75 * 2
                capital += bet * 6.75 * 2
            else:
                game_outcomes[0] += 1
                round_history.append(bet * 6.75)
                win += 1
                winnings += bet * 6.75
                capital += bet * 6.75

        if lets_play == 3:
            if destiny == 3:
                game_outcomes[3] += 1
                round_history.append(bet * 3 * 2)
                win += 1
                winnings += bet * 3 * 2
                capital += bet * 3 * 2
            else:
                game_outcomes[2] += 1
                round_history.append(bet * 3)
                win += 1
                winnings += bet * 3
                capital += bet * 3

        if lets_play == 11:
            if destiny == 4:
                game_outcomes[3] += 1
                round_history.append(bet * 3 * 2)
                win += 1
                winnings += bet * 3 * 2
                capital += bet * 3 * 2
            else:
                game_outcomes[2] += 1
                round_history.append(bet * 3)
                win += 1
                winnings += bet * 3
                capital += bet * 3
        if lets_play == -1:
            game_outcomes[4] += 1
            round_history.append(-1.25)
            winnings -= 1.25
            capital -= 1.25
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
    x_values = ["2,12", "2,12double", "3,11", "3,11double", "lose"]
    plt.vlines(x_values, 0, probabilities)
    plt.show()


if __name__ == '__main__':
    main()
