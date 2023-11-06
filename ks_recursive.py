def ks_recursive(items: list[tuple[int, int]], capacity: int) -> int:
    # Base case: If there are no items or no remaining capacity, the maximum value is 0
    if not items or capacity == 0:
        return 0

    # Start with the last item in the list index i
    i = len(items)

    # If the weight of the last item exceeds the current capacity don't include it
    if items[i - 1][0] > capacity:
        return ks_recursive(items[:-1], capacity)
    else:
        # Calculate the maximum value by either taking or leaving the last item
        take_item = ks_recursive(items[:-1], capacity - items[i - 1][0]) + items[i - 1][1]
        leave_item = ks_recursive(items[:-1], capacity)
        return max(take_item, leave_item)
