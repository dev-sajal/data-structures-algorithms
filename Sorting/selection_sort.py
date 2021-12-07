from utils import get_operator, swap


def sort(array: list, ascending: bool=True)-> list:
    """
    Idea:
    Sort at the start and as each iteration goes, that number of
    elements from the start are in sorted order.
    Algorithm:
    Repeat until empty
        Find the min (ascending) in the array and replace it with the first element
        in the list
    done
    """
    op = get_operator(ascending)
    array_size = len(array)
    for i in range(array_size):
        key = i
        for j in range(i+1, array_size):
            key = j if op(array[j], array[key]) else key
        array = swap(array, i, key)
    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Selection Sort (ascending):", sort(arr))
    print("Selection Sort (descending):", sort(arr, False))
