import random


def get_input_data():
    n1 = 3
    n2 = 4
    n3 = 3
    return n1, n2, n3


def model(n1, n2, n3):
    n = n1 + n2 + n3
    print("n =", n)
    print("n1 =", n1)
    print("n2 =", n2)
    print("n3 =", n3)
    N = 100000
    count = 0
    students = [1 for _ in range(n1)] + [2 for _ in range(n1, n1 + n2)] + [3 for _ in range(n1 + n2, n)]
    for j in range(N):
        first_student = random.randint(0, n - 1)
        second_student = random.randint(0, n - 1)
        while students[second_student] == students[first_student]:
            second_student = random.randint(0, n - 1)
        if students[first_student] == 3 or students[second_student] == 3:
            count += 1

    print('Вероятность того, что среди двух выбранных студентов\n'
          '(один из которых учится дольше другого) один учится третий год:\n'
          f'Моделирование: P = {count / N:.05f}\n'
          f'Аналитически: P = {((n1 + n2) * n3) / (n1 * n2 + (n1 + n2) * n3):.05f}')


def main():
    model(*get_input_data())


if __name__ == '__main__':
    main()
