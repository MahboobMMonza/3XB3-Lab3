from knapsack import *


def test1(solver: callable):
    choices: list[tuple[int, int]] = [(6, 5), (5, 6), (6, 4), (6, 6), (3, 5), (7, 2)]
    cap: int = 15
    assert solver(choices, cap) == 17
    print('PASS 1')


def test2(solver: callable):
    choices: list[tuple[int, int]] = [(1, 10 ** 9) for _ in range(5)]
    cap: int = 5
    assert solver(choices, cap) == (5 * 10 ** 9)
    print('PASS 2')


def test3(solver: callable):
    choices: list[tuple[int, int]] = [(3, 30), (4, 50), (5, 60)]
    cap: int = 8
    assert solver(choices, cap) == 90
    print('PASS 3')


def main():
    solvers = [ks_bottom_up, ks_top_down, ks_brute_force, ks_recursive]
    for solver in solvers:
        print('*********', solver.__name__, '*********')
        test1(solver)
        test2(solver)
        test3(solver)
        print('#########', solver.__name__, '#########')


if __name__ == '__main__':
    main()
