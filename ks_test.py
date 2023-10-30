from knapsack import *


def test1(solver: callable):
    choices: list[tuple[int, int]] = [(5, 6), (6, 5), (4, 6), (6, 6), (5, 3), (2, 7)]
    cap: int = 15
    assert solver(choices, cap) == 17
    print('PASS 1')


def test2(solver: callable):
    choices: list[tuple[int, int]] = [(10 ** 9, 1) for _ in range(5)]
    cap: int = 5
    assert solver(choices, cap) == (5 * 10 ** 9)
    print('PASS 2')


def test3(solver: callable):
    choices: list[tuple[int, int]] = [(30, 3), (50, 4), (60, 5)]
    cap: int = 8
    assert solver(choices, cap) == 90
    print('PASS 3')


def main():
    solvers = [ks_bottom_up, ks_brute_force]
    for solver in solvers:
        print('*********', solver.__name__, '*********')
        test1(solver)
        test2(solver)
        test3(solver)
        print('#########', solver.__name__, '#########')


if __name__ == '__main__':
    main()
