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
            # If this is the last item, since the highest weight is filled first, we can return answer
            if i + 1 == len(items):
                break

    return table[capacity]


def ks_brute_force(items: list[tuple[int, int]], capacity: int) -> int:
    max_val: int = 0

    # Try every combination. There are 2^n combinations possible, and these can be represented in an
    # integer with n bits. If the ith bit is 1, we take the ith item in the current combination, and
    # leave it if the bit is 0. We need to check that the weight doesn't exceed the capacity as well.

    for combination in range(1 << len(items)):
        value, weight = 0, 0
        for item_idx in range(len(items)):
            # Take the current item if its bit is a 1
            if combination & (1 << item_idx):
                value, weight = value + items[item_idx][0], weight + items[item_idx][1]

        # Update max cap
        if weight <= capacity:
            max_val = max(max_val, value)

    return max_val


def ks_top_down(items: list[tuple[int, int]], capacity: int) -> int:
    num_items = len(items)

    # Initialize a memorization table
    memorization_table = [[-1] * (capacity + 1) for _ in range(num_items + 1)]

    # Define a recursive function to calculate the optimal value
    def recursive_knapsack(index, weight):

        # If the value for this combination has already been computed, then return the combination
        if memorization_table[index][weight] >= 0:
            return memorization_table[index][weight]

        # Base case: If there are no items or capacity left, then return 0
        if index == 0 or weight == 0:
            optimal_value = 0

        # If the weight of the current item is less than or equal to the remaining capacity
        # Choose the max between taking the current item or not taking it
        elif items[index - 1][1] <= weight:
            optimal_value = max(recursive_knapsack(index - 1, weight - items[index - 1][1]) + items[index - 1][0], recursive_knapsack(index - 1, weight))
        else:
            # If the weight of the current item exceeds the remaining capacity, move on to the next item
            optimal_value = recursive_knapsack(index - 1, weight)

        # Cache the computed value for the next reference
        memorization_table[index][weight] = optimal_value
        return optimal_value

    # Call the recursive function with the total number of items and the total capacity
    result = recursive_knapsack(num_items, capacity)
    return result
