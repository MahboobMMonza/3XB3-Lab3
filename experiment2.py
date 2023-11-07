import timeit
from knapsack import *
from utilities import *


#Create experiment where bottom-up approach is faster
def experiment2a():
    capacity = 35000
    total_items = 200
    num_experiments = 10
    weight_range = (8000, 10000)
    value_range = (1000, 5000)
    items = generate_random_items(total_items, weight_range, value_range)
    num_items = list(range(5, 202, 5))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(num_experiments):
            items = items[:item_count]

            # Measure the runtime for ks_topdown
            start_time = timeit.default_timer()
            ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_avg_time += (end_time - start_time)

            # Measure the runtime for ks_bottom-up
            start_time = timeit.default_timer()
            ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_avg_time += (end_time - start_time)

        # Calculate average runtimes
        TD_avg_time /= num_experiments
        BU_avg_time /= num_experiments

        runtimes_TD.append(TD_avg_time)
        runtimes_BU.append(BU_avg_time)

    create_plot(num_items, [runtimes_TD, runtimes_BU],
                legend_labels=["ks_top_down", "ks_bottom_up"],
                title="Knapsack Problem Runtimes (Recursion vs Brute Force)",
                description="10 reps for lists of size 20,where values range randomly from 1000-2000 and weights range randomly from 50-75",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=2.5,
                )


def experiment2b():
    capacity = 35000
    total_items = 20
    num_experiments = 10
    weight_range = (1000, 5000)
    value_range = (8000, 10000)
    items = generate_random_items(total_items, weight_range, value_range)
    num_items = list(range(1, 21))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(num_experiments):
            items = items[:item_count]

            # Measure the runtime for ks_topdown
            start_time = timeit.default_timer()
            ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_avg_time += (end_time - start_time)

            # Measure the runtime for ks_bottom-up
            start_time = timeit.default_timer()
            ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_avg_time += (end_time - start_time)

        # Calculate average runtimes
        TD_avg_time /= num_experiments
        BU_avg_time /= num_experiments

        runtimes_TD.append(TD_avg_time)
        runtimes_BU.append(BU_avg_time)

    create_plot(num_items, [runtimes_TD, runtimes_BU],
                legend_labels=["ks_top_down", "ks_bottom_up"],
                title="Knapsack Problem Runtimes (Recursion vs Brute Force)",
                description="10 reps for lists of size 20,where values range randomly from 1000-2000 and weights range randomly from 50-75",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=2.0,
                show_ticks=False)


def main():
    experiment2a()
    experiment2b()


if __name__ == '__main__':
    main()
