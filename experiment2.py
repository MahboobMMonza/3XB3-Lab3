import timeit
from knapsack import *
from utilities import *


# Create experiment where top-down approach is faster
def experiment2a():
    capacity = 20000
    min_value = 1
    max_value = 30
    step = 1
    reps = 20
    weight_range = (800, 2000)
    value_range = (1000, 5000)
    num_items = list(range(min_value, max_value + 1))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(reps):
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
        TD_avg_time /= reps
        BU_avg_time /= reps

        runtimes_TD.append(TD_avg_time)
        runtimes_BU.append(BU_avg_time)

    create_plot(num_items, [runtimes_TD, runtimes_BU],
                legend_labels=["ks_top_down", "ks_bottom_up"],
                title=f"Runtime Comparisons of Top-Down & Bottom-Up Implementations of the Knapsack Problem",
                description=f"{(max_value + 1 - min_value) // step} increments up to {max_value} from {min_value} with {reps}"
                            f" repetitions per increment. Values range from {value_range[0]} to {value_range[1]}"
                            f"; Weights range from {weight_range[0]} to {weight_range[1]}",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=1.75,
                )


def experiment2b():
    capacity = 800
    min_value = 30
    max_value = 80
    step = 5
    reps = 20
    weight_range = (50, 200)
    value_range = (1000, 5000)
    num_items = list(range(min_value, max_value + 1, step))

    # Lists to store the runtimes for ks_rec and ks_brute_force
    runtimes_TD = []
    runtimes_BU = []

    for item_count in num_items:
        TD_avg_time = 0
        BU_avg_time = 0

        for _ in range(reps):
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
        TD_avg_time /= reps
        BU_avg_time /= reps

        runtimes_TD.append(TD_avg_time)
        runtimes_BU.append(BU_avg_time)

    create_plot(num_items, [runtimes_TD, runtimes_BU],
                legend_labels=["ks_top_down", "ks_bottom_up"],
                title=f"Runtime Comparisons of Top-Down & Bottom-Up Implementations of the Knapsack Problem",
                description=f"{(max_value + 1 - min_value) // step} increments up to {max_value} from {min_value} with {reps}"
                            f" repetitions per increment. Values range from {value_range[0]} to {value_range[1]}"
                            f"; Weights range from {weight_range[0]} to {weight_range[1]}",
                x_label="Number of Items",
                y_label="Runtime(s)",
                scale=2.2)


def main():
    experiment2a()
    experiment2b()


if __name__ == '__main__':
    main()
