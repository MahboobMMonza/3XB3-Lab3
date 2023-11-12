"""
Optimal Substructure

# of bricks => m
# of levels => n (translating n - 1 on the actual search into N)

Note: This problem is the same as finding some level equivalent to k* - 1 within levels 0...n - 1 (where level 0
signifies there is no level that won't break the brick). This is because k* is the first level at which the brick will
break, and so k* - 1 is the last level for which it won't break. Since a brick is guaranteed to break at some level
between 1 and n, it is guaranteed to break at n, so we only need to consider levels 0 to n - 1.

Case 1:
If m >= floor(log_2(n - 1)) + 1, then we can binary search without issues. I will need floor(log_2(n - 1)) + 1 runs on
the machine to know what k* is (as stated in the lab instructions). Note that log_2(0) = 0 for our purposes, and integer
division is assumed. The only exception would be that no testing would be required if there is only 1 level.

Case 2:
If m = 1, then our only option is to go up one-by-one until it doesn't break. The last non-breaking value can be n - 1,
so n - 1 tests are required at worst case.

Case 3:
When there are not enough bricks to do a binary search, we "try" every level and see which one gave the lowest
worst-case. At each level w, if the brick breaks, we would need to check w - 1 levels with one less brick. If the brick
doesn't break, then we need to check N - w levels with the same number of bricks. Of these two options, we choose the
one with the highest total as that is the worst-case and add 1 to it (to represent the force test at level w). Then,
among all N levels, we choose the one with the lowest worst-case if the first brick was tested at that level first to
determine the lowest number of tests necessary to find k* - 1, which is the same as the number of bricks needed to find
k*.

========================================================================================================================
Recurrence Relation

Test(i, j) => worst-case tests needed with j bricks and i levels. The levels here are from 0 to N (= n - 1), NOT 1 to n

Base Case 1:
With i levels and 1 brick, i levels have to be tested one-by-one, so Test(i, 1) = i.

Base Case 2.1:
With 1 level and j >= 1 bricks, only the one level needs to be tested. Similarly, if there are 0 levels and j >= 1
bricks, then no levels need to be tested. So Test(1, j) = 1 and Test(0, j) = 0 for j >= 1.

Base Case 2.2:
With no bricks, no levels can be tested. This won't mess up calculations because in each level's worst case, we take the
maximum. Test(i, 0) = 0.

Otherwise, the rules for Case 3 apply, and for i levels and j bricks:
Test(i, j) = min(1 + max(Test(N - k, j), Test(k - 1, j - 1))) for all k in [1, i]

There will be many cases of overlapping sub-problems that would require recalculation if not cached, so top-down will be
an easy way to tackle the problem, as cases will be solved when they are first encountered.

########################################################################################################################
Test(i, j):
* Test(i, 1) = i
* Test(1 >= i >= 0, j >= 1) = i
* Test(i, 0) = 0
* Test(i, j) = min(1 + max(Test(N - k, j), Test(k - 1, j - 1))) for all k in [1, i]
########################################################################################################################
"""


def test_levels_helper(i: int, j: int, tests: list[list[int]], next_level: list[list[int]]) -> int:
    # Answer is already computed if tests[j][i] <= i (since before it was initialized to n + 1)
    if tests[j][i] <= i:
        return tests[j][i]

    # Try every level from 1 to i to see which one has the lowest number of tests worst case
    for k in range(1, i + 1):
        # Calculate the new worst-case if this force setting level was tested. If it is better, then record this level
        # as the best starting level with i setting levels.
        old_tests = tests[j][i]
        tests[j][i] = min(tests[j][i], 1 + max(test_levels_helper(i - k, j, tests, next_level),
                                               test_levels_helper(k - 1, j - 1, tests, next_level)))
        if tests[j][i] < old_tests:
            next_level[j][i] = k

    return tests[j][i]


def test_levels(n: int, m: int) -> (list[list[int]], list[list[int]]):
    # n => Number of levels
    # m => number of bricks

    # Initialize memoization tables: TESTS for worst-case runs, NEXT_LEVEL for the next level to choose
    # Note that in the recurrence relation, it was identified as Test(i, j), but will be stored as Test[j][i]
    tests = [[n + 1] * n for _ in range(m + 1)]
    # Naively, the first force level to test is 1
    next_level = [[1] * n for _ in range(m + 1)]

    # Base cases
    tests[0][0] = 0
    next_level[0][0] = 0
    for i in range(1, n):
        tests[1][i] = i
        tests[0][i] = 0
        next_level[0][i] = 0

    for j in range(1, m + 1):
        tests[j][1] = 1
        tests[j][0] = 0
        next_level[j][0] = 0

    # Make recursive call to helper and get result
    test_levels_helper(n - 1, m, tests, next_level)
    return tests, next_level


def num_of_wc_runs(n: int, m: int) -> int:
    # n => Number of levels
    # m => number of bricks
    tests = test_levels(n, m)[0]
    return tests[m][n - 1]


def next_setting(n: int, m: int) -> int:
    # n => Number of levels
    # m => number of bricks
    settings = test_levels(n, m)[1]
    return settings[m][n - 1]
