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
one with the highest total as that is the worst-case and add 1 to it (to signify the force test at the specific level).
Then, among all N levels, we choose the one with the lowest worst-case if the first brick was tested at that level first
to determine the lowest number of tests necessary to find k* - 1, which is the same as the number of bricks needed to
find k*.

========================================================================================================================
Recurrence Relation

Test(i, j) => worst-case tests needed with j bricks and i levels. The levels here are from 0 to N (= n - 1), NOT 1 to n

Base Case 1:
With i levels and 1 brick, i levels have to be tested one-by-one, so Test(i, j) = i.

Base Case 2.1:
With 1 level and j >= 1 bricks, only the one level needs to be tested. Similarly, if there are 0 levels and j >= 1
bricks, then no levels need to be tested. So Test(i, 1) = 1 and Test(i, 0) = 0.

Base Case 2.2:
With no bricks, no levels can be tested. This won't mess up calculations because in each level's worst case, we take the
maximum. Test(i, 0) = 0.

Otherwise, the rules for Case 3 apply, and for i levels and j bricks:
Test(i, j) = min(1 + max(Test(N - k, j), Test(k - 1, j - 1))) for all k in [2, i]

There will be many cases of overlapping sub-problems that would require recalculation if not cached, so top-down will be
an easy way to tackle the problem, as cases will be solved when they are first encountered.

########################################################################################################################
Test(i, j):
* Test(i, 1) = i
* Test(1 >= i >= 0, j > 1) = i
* Test(i, 0) = 0
* Test(i, j) = min(1 + max(Test(N - k, j), Test(k - 1, j - 1))) for all k in [2, i]
########################################################################################################################
"""
