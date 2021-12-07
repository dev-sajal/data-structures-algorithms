from utils import find_max_index, find_min_index


def sort(array: list, size: int, ascending:bool=True)-> list:
    min_element = array[find_min_index(array)]
    max_element = array[find_max_index(array)]

    count_array_size = max_element + 1 - min_element
    count = [0]*(count_array_size)
    for element in array:
        count[element - min_element] += 1

    for idx in range(1, count_array_size):
        count[idx] += count[idx-1]

    sorted_array = [0]*size
    for idx in range(size-1, -1, -1):
        count[array[idx] - min_element] -= 1
        sorted_array[count[array[idx] - min_element]] = array[idx]

    if ascending:
        array = sorted_array
    else:
        for idx in range(size-1, -1, -1):
            array[size-1-idx] = sorted_array[idx]
    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Counting Sort (ascending):", counting_sort(arr, arr_size))
    print("Counting Sort (descending):",counting_sort(arr, arr_size, False))
