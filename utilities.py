import random

import matplotlib.pyplot as plt


def create_plot(x_vals: list,
                y_vals: list[list],
                legend_labels: list[str],
                title: str,
                description: str,
                x_label: str,
                y_label: str,
                scale: float = 1,
                show_ticks: bool = True) -> None:
    height, width = plt.figure().get_figheight(), plt.figure().get_figwidth()
    plt.figure(figsize=(scale * width, scale * height))
    for yv, legend in zip(y_vals, legend_labels):
        plt.plot(x_vals, yv, linewidth=2, label=legend, marker='o')

    plt.xlabel(x_label)
    if show_ticks:
        plt.xticks(x_vals)
    plt.ylabel(y_label)
    plt.suptitle(title, fontsize=14)
    plt.title(description, fontsize=10)
    plt.legend(fontsize=10)
    plt.show()

def generate_random_items(num_items: int, weight_range: tuple[int, int], value_range: tuple[int, int]) -> list[
    tuple[int, int]]:
    items = []

    for _ in range(num_items):
        # Generate random values and weights within the specified ranges
        value = random.randint(value_range[0], value_range[1])
        weight = random.randint(weight_range[0], weight_range[1])
        items.append((weight, value))

    return items

