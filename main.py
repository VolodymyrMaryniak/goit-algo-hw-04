import timeit
import random

import bubble_sort
import insertion_sort
import quick_sort
import selection_sort
import merge_sort
import shell_sort
import radix_sort


def measure_time(sort_function, data):
    return timeit.timeit(lambda: sort_function(data[:]), number=5)


def main():
    data_small = [random.randint(0, 100000) for _ in range(1000)]
    data_medium = [random.randint(0, 100000) for _ in range(10000)]

    sorting_algorithms = [
        ("Bubble Sort", bubble_sort.bubble_sort),
        ("Insertion Sort", insertion_sort.insertion_sort),
        ("Selection Sort", selection_sort.selection_sort),
        ("Merge Sort", merge_sort.merge_sort),
        ("Quick Sort", quick_sort.quick_sort),
        ("Shell Sort", shell_sort.shell_sort),
        ("Radix Sort", radix_sort.radix_sort),
        ("Python (sorted)", sorted),
        ("Python (list.sort)", list.sort),
    ]

    print(f"{'Algorithm':<20} | {'Time small data': <20} | {'Time medium data': <20}")
    print(f"{'-'*20} | {'-'*20} | {'-'*20}")

    for name, func in sorting_algorithms:
        time_small = measure_time(func, data_small)
        time_medium = measure_time(func, data_medium)
        print(f"{name:<20} | {time_small:<20.5f} | {time_medium:<20.5f}")

    data_large = [random.randint(0, 1000000) for _ in range(1000000)]
    large_data_sorting_algorithms = [
        ("Merge Sort", merge_sort.merge_sort),
        ("Quick Sort", quick_sort.quick_sort),
        ("Shell Sort", shell_sort.shell_sort),
        ("Radix Sort", radix_sort.radix_sort),
        ("Python (sorted)", sorted),
        ("Python (list.sort)", list.sort),
    ]

    print(f"{'Algorithm':<20} | {'Time large data':<20}")
    print(f"{'-'*20} | {'-'*20}")
    for name, func in large_data_sorting_algorithms:
        time_large = measure_time(func, data_large)
        print(f"{name:<20} | {time_large:<20.5f}")


if __name__ == "__main__":
    main()
