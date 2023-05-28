from game import *


def round():
    bet = 1
    while True:
        big_point = roll()
        if big_point == 6:
            return bet
        if big_point == 7:
            return -bet


def game(experiment):
    bet = 1
    win = 0
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
            round_history.append(1)
            win += 1
            winnings += bet
            capital += bet
        if lets_play == -1:
            round_history.append(-1)
            winnings -= bet
            capital -= bet
        average_winnings.append(winnings / (i * bet))
    list_intervals_down, list_intervals_up = building_confidence_probability(round_history, average_winnings)
    print_results(win, experiment, winnings, bet, overall_length, game_number, round_history)
    return list_intervals_down, list_intervals_up, average_winnings, round_history


def main():
    experiment = 1_000_000
    list_intervals_down, list_intervals_up, average_winnings, round_history = game(experiment)
    build_graphic(list_intervals_down, list_intervals_up, average_winnings, experiment, round_history, (-1, 1))


if __name__ == '__main__':
    main()
