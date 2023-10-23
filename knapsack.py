def ks_bottom_up(items: list[tuple[int, int]], capacity: int) -> int:
    # items[i] => (value, weight)

    # We can actually reduce the table to a single row for the capacity by looping in reverse,
    # updating values until the current weight is lower than the weight of the object. This is
    # because before each item, the jth index already contains the best choices up to item i - 1
    # for the current weight, so we can just keep it if it is optimal, or overwrite it if it
    # isn't. This only works for something like knapsack, because it relies only on the best choice
    # for the item before the current item.

    table = [0 for _ in range(capacity + 1)]
    # i from 0...n - 1 (inclusive)
    for i in range(len(items)):
        # j from capacity...weight[j] (inclusive)
        for j in range(capacity, items[i][1] - 1, -1):
            # Index is offset by 1
            # Optimal choice is not taking the item, or taking the item + best prev choice
            table[j] = max(table[j], table[j - items[i][1]] + items[i][0])

    return table[capacity]

