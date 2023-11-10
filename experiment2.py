import timeit
from knapsack import *
from utilities import *


# Create experiment where top-down approach is faster
def experiment2a():
    capacity = 20000
    max_items = 30
    num_experiments = 20
    weight_range = (800, 2000)
    value_range = (1000, 5000)
    num_items = list(range(1, max_items + 1))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(num_experiments):
            items = generate_random_items(item_count, weight_range, value_range)

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
                title=f"Runtime Comparisons of Top-Down & Bottom-Up Implementations of the Knapsack Problem",
                description=f"{num_experiments} reps for number of items up to {max_items},where values range randomly from {value_range[0]} to {value_range[1]} and "
                            f" weights range randomly from {weight_range[0]} to {weight_range[1]}, with capacity = {capacity} ",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=1.75,
                )


def experiment2b():
    capacity = 800
    max_items = 80
    num_experiments = 20
    weight_range = (50, 200)
    value_range = (1000, 5000)
    num_items = list(range(30, max_items + 1, 5))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(num_experiments):
            items = generate_random_items(item_count, weight_range, value_range)

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
                title=f"Runtime Comparisons of Top-Down & Bottom-Up Implementations of the Knapsack Problem",
                description=f"{num_experiments} reps for number of items up to {max_items}, incremented by 5,where values range randomly from {value_range[0]} to {value_range[1]}, incrementing by 5 "
                            f" and weights range randomly from {weight_range[0]} to {weight_range[1]} with capacity = {capacity}",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=2.2)


def main():
    experiment2a()
    #experiment2b()


if __name__ == '__main__':
    main()
