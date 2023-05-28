from game import *

come_point = 0
bet = False
plus = 0


def round():
    global come_point, bet, plus
    global bet
    point = roll()
    if (point == come_point) and bet:
        bet = False
        return -1
    if (point == 7) and bet:
        bet = False
        return 1
    if point in (2, 3, 12, 11, 7):
        return 2
    # ставка
    if not bet:
        bet = True
        comeout_roll = roll()
        come_point = comeout_roll
        if comeout_roll in (7, 11):
            bet = False
            return -1
        if comeout_roll in (2, 3):
            bet = False
            return 1
        if comeout_roll == 12:
            bet = False
            return 0
        if comeout_roll == point:
            return 2

    while True:
        comeout_roll = roll()
        if comeout_roll == come_point:
            bet = False
            return -1
        if comeout_roll == point:
            return 2
        if comeout_roll == 7:
            bet = False
            return 1


def game(experiment):
    wager = 1
    win = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    average_winnings = []
    round_history = []
    i = 1
    winnings = 0
    while i < experiment:
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play == 2:
            continue
        game_length += 1
        if lets_play == 0:
            round_history.append(0)
        if lets_play == 1:
            round_history.append(1)
            win += 1
            winnings += 1
            capital += 1
        if lets_play == -1:
            round_history.append(-1)
            winnings -= 1
            capital -= 1

        i += 1
        average_winnings.append(winnings / (i * wager))

    list_intervals_down, list_intervals_up = building_confidence_probability(round_history, average_winnings)
    print_results(win, experiment, winnings, 1, overall_length, game_number,round_history)
    return list_intervals_down, list_intervals_up, average_winnings, round_history


def main():
    experiment = 1_000_000
    list_intervals_down, list_intervals_up, average_winnings, round_history = game(experiment)
    build_graphic(list_intervals_down, list_intervals_up, average_winnings, experiment, round_history, (-1, 0, 1))


if __name__ == '__main__':
    main()
