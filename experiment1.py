import timeit
from knapsack import ks_recursive, ks_brute_force
from utilities import *


def experiment1():
    capacity = 915
    min_value = 1
    max_value = 20
    step = 1
    reps = 20
    weight_range = (50, 75)
    value_range = (1000, 2000)
    items = generate_random_items(max_value, weight_range, value_range)
    num_items = list(range(min_value, max_value + 1))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_rec = []
    runtimes_brute_force = []

    for item_count in num_items:
        rec_avg_time = 0
        brute_force_avg_time = 0

        for _ in range(reps):
            items = generate_random_items(item_count, weight_range, value_range)

            # Measure the runtime for ks_rec
            start_time = timeit.default_timer()
            ks_recursive(items, capacity)
            end_time = timeit.default_timer()
            rec_avg_time += (end_time - start_time)

            # Measure the runtime for ks_brute_force
            start_time = timeit.default_timer()
            ks_brute_force(items, capacity)
            end_time = timeit.default_timer()
            brute_force_avg_time += (end_time - start_time)

        # Calculate average runtimes
        rec_avg_time /= reps
        brute_force_avg_time /= reps

        runtimes_rec.append(rec_avg_time)
        runtimes_brute_force.append(brute_force_avg_time)

    create_plot(num_items, [runtimes_rec, runtimes_brute_force],
                legend_labels=["ks_rec", "ks_brute_force"],
                title="Runtime Comparisons of Recursive & Brute-Force Implementations of the Knapsack Problem ",
                description=f"{(max_value + 1 - min_value) // step} increments up to {max_value} from {min_value} with {reps}"
                            f" repetitions per increment. Values range from {value_range[0]} to {value_range[1]}"
                            f"; Weights range from {weight_range[0]} to {weight_range[1]} and capacity set to {capacity}",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=1.75)


def main():
    experiment1()


if __name__ == '__main__':
    main()
