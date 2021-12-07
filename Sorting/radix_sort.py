def _counting_sort(array: list, size: int, digit_place: int)->list:
    """
    An internal function for Radix Sort which sort on basis of digit_place
    rather than whole number like in the original Count Sort.

    Provides an upper bound on the number of buckets or size of the count array
    """
    # Digits will be between 0-9, can be reduced to max digit present
    count_array_size = 10
    count = [0]*(count_array_size)

    for element in array:
        element //= digit_place
        element %= 10
        count[element] += 1

    for idx in range(1, count_array_size):
        count[idx] += count[idx-1]

    sorted_array = [0]*size
    for idx in range(size-1, -1, -1):
        index = array[idx] // digit_place
        index %= 10
        count[index] -= 1
        sorted_array[count[index]] = array[idx]

    # To return back sorted in the same array
    array = sorted_array
    return array


def sort(array: list, size: int, ascending: bool=True)-> list:
    max_element = array[find_max_index(array)]
    digit_place = 1
    while (max_element // digit_place > 0):
        array = _counting_sort(array, size, digit_place)
        digit_place *= 10

    if not ascending:
        array = array[::-1]
    return array


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    arr_size = len(arr)
    print("Initial array:", arr)

    print("--"*40)
    print("Radix Sort using count sort (ascending):", sort(arr, arr_size))
    print("Radix Sort using count sort (descending):",sort(arr, arr_size, False))
