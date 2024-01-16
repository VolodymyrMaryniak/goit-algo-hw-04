def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1

    result += left_arr[left_idx:]
    result += right_arr[right_idx:]

    return result


if __name__ == "__main__":
    arr = [5, 2, 1, 3, 4]
    print(merge_sort(arr))
