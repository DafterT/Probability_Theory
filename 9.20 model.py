import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

############
MAX_NUM = 5_000_000
n = 10
m = 20
############


def model():
    sumPoints = 0
    for i in range(n):
        sumPoints += random.randint(1, 6)
    return sumPoints <= m


def solve():
    return 0.0029


def print_table_with_graph(x, y, modaOfY, analytic, name):
    values = []
    for item in modaOfY.items():
        values.append(item)
    values.sort(key=lambda v: v[1], reverse=True)
    print(f'Аналитически ответ: {analytic}')
    th = ['МОДА', 'ЗНАЧЕНИЕ', 'ПОГРЕШНОСТЬ']
    table = PrettyTable(th)
    for v in values[:3]:
        table.add_row([v[1], "{0:.10f}".format(v[0]), "{0:.6f}".format(abs(analytic - v[0]))])
    print(table)
    plt.xlabel('Кол-во экспериментов', color='black')
    plt.ylabel('Вероятность хорошего исхода', color='black')
    plt.grid(True)
    plt.plot(x, y)
    plt.savefig(name)
    plt.show()


def main():
    allResults = 0
    goodResults = 0
    x = []
    y = []
    moda = {}
    while allResults != MAX_NUM:
        if model():
            goodResults += 1
        allResults += 1
        x.append(allResults)
        value = goodResults / allResults
        y.append(value)
        if moda.get(value) is None:
            moda[value] = 0
        moda[value] += 1

    print_table_with_graph(x, y, moda, solve(), "pictures/9.20.Chance.jpg")


if __name__ == '__main__':
    main()
