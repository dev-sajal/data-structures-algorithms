from utils import get_operator


def sort(array: list, low: int, high: int, ascending: bool=True)-> list:
    op = get_operator(ascending)
    if high > low:
        mid = (high + low) // 2

        # can use direct len function, but want to mimick C type behaviour
        left_array_length = mid + 1 - low
        right_array_length = high - mid

        # When dividing right side of the array, it will cause trouble as
        # bounds will be from original array but the divided array size would
        # be small
        mid -= low
        left_array = array[:mid+1]
        right_array = array[mid+1:]

        # Reversing back to previous value for further split calls
        mid += low
        sort(left_array, low, mid, op)
        sort(right_array, mid+1, high, op)


        # Merging Process
        left_subarray_indexer = right_subarray_indexer = array_indexer = 0
        while (left_subarray_indexer < left_array_length) and \
                (right_subarray_indexer < right_array_length):
            if op(left_array[left_subarray_indexer], right_array[right_subarray_indexer]):
                array[array_indexer] = left_array[left_subarray_indexer]
                left_subarray_indexer += 1
            else:
                array[array_indexer] = right_array[right_subarray_indexer]
                right_subarray_indexer += 1
            array_indexer += 1

        while left_subarray_indexer < left_array_length:
            array[array_indexer] = left_array[left_subarray_indexer]
            left_subarray_indexer += 1
            array_indexer += 1

        while right_subarray_indexer < right_array_length:
            array[array_indexer] = right_array[right_subarray_indexer]
            right_subarray_indexer += 1
            array_indexer += 1

    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Merge Sort (ascending):", sort(arr, 0, arr_size-1))
    print("Merge Sort (descending):",sort(arr, 0, arr_size-1, False))
