import numpy as np
import matplotlib.pyplot as plt


def get_input_data():
    probability = 1 / 2
    time_signal_interval = 5
    time_delay = 16
    return probability, time_signal_interval, time_delay


def generate_signals(probability, time_interval, delay, break_time):
    time = 0
    count_signals = 1
    while time + delay <= break_time:
        if np.random.random() < probability:
            return time + delay, count_signals + 3
        count_signals += 1
        time += time_interval
    return -1


def simulate(num_trials, probability, time_interval, delay, break_time):
    signal_times = [0] * break_time
    count_signals_mas = [0] * break_time
    counter = 0
    for _ in range(num_trials):
        signal_time, count_signals = generate_signals(probability, time_interval, delay, break_time)
        if signal_time != -1:
            counter += 1
            signal_times[signal_time] += 1
            count_signals_mas[count_signals] += 1

    return signal_times, count_signals_mas, counter


def main():
    count_simulations = 1_000_000
    break_time = 200
    probability, time_signal_interval, time_delay = get_input_data()
    signals, count_signals_mas, count_signals = simulate(count_simulations, probability, time_signal_interval,
                                                         time_delay, break_time)
    plt.plot(range(break_time), [signal / count_signals for signal in signals])
    plt.title('Вероятность от времени')
    plt.xlabel('Время', color='black')
    plt.ylabel('Вероятность что произойдет включение', color='black')
    plt.savefig('pictures/10.7.Chance_1.jpg')
    plt.show()

    plt.plot(range(break_time // time_signal_interval),
             [count / count_signals for count in count_signals_mas[:break_time // time_signal_interval]], color='g')
    plt.plot(range(break_time // time_signal_interval),
             [0, 0, 0, 0, *[2 ** (3 - i) for i in range(4, break_time // time_signal_interval)]], color='r')
    plt.title('Вероятность от числа сигналов')
    plt.xlabel('Количество сигналов', color='black')
    plt.ylabel('Вероятность что произойдет включение', color='black')
    plt.savefig('pictures/10.7.Chance_2.jpg')
    plt.show()


if __name__ == '__main__':
    main()
