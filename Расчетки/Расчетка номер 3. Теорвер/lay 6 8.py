from game import *


def round():
    while True:
        single_roll = roll()
        if single_roll == 6:
            return -1
        if single_roll == 7:
            return 1


def game(experiment):
    bet = 6
    win = 0

    average_winnings = []
    round_history = []
    capital = bet
    game_number = 0
    game_length = 0
    overall_length = 0

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
            round_history.append(5 * 0.95)
            win += 1
            winnings += 5 * 0.95
            capital += 5 * 0.95

        if lets_play == -1:
            round_history.append(-1 * bet)
            winnings -= bet
            capital -= bet

        average_winnings.append(winnings / (i * bet))
    list_intervals_down, list_intervals_up = building_confidence_probability(round_history, average_winnings)
    print_results(win, experiment, winnings, bet, overall_length, game_number, round_history)
    return list_intervals_down, list_intervals_up, average_winnings, round_history


def main():
    experiment = 1_000_000
    list_intervals_down, list_intervals_up, average_winnings, round_history = game(experiment)
    build_graphic(list_intervals_down, list_intervals_up, average_winnings, experiment, round_history, (-6, 5 * 0.95))


if __name__ == '__main__':
    main()
