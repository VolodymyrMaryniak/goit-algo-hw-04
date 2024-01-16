def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [5, 2, 1, 3, 4]
    print(quick_sort(arr))
