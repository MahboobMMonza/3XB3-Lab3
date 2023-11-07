import timeit
from knapsack import ks_recursive, ks_brute_force
from utilities import *


def experiment1():
    capacity = 915
    total_items = 20
    num_experiments = 10
    weight_range = (50, 75)
    value_range = (1000, 2000)
    items = generate_random_items(total_items, weight_range, value_range)
    num_items = list(range(1, 21))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_rec = []
    runtimes_brute_force = []

    for item_count in num_items:
        rec_avg_time = 0
        brute_force_avg_time = 0

        for _ in range(num_experiments):
            items = items[:item_count]

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
        rec_avg_time /= num_experiments
        brute_force_avg_time /= num_experiments

        runtimes_rec.append(rec_avg_time)
        runtimes_brute_force.append(brute_force_avg_time)

    create_plot(num_items, [runtimes_rec, runtimes_brute_force],
                legend_labels=["ks_rec", "ks_brute_force"],
                title="Knapsack Problem Runtimes (Recursion vs Brute Force)",
                description="10 reps for lists of size 20,where values range randomly from 1000-2000 and weights range randomly from 50-75",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=1.5)


def main():
    experiment1()


if __name__ == '__main__':
    main()
