from random import randint
from utils import get_operator, swap


def get_pivot(lower: int, upper: int)-> int:
    return randint(lower, upper)


def partition(array: list, start: int, end: int, op: callable)->int:
    # Get Random Pivot Element
    pivot = get_pivot(start, end)

    # Swap the pivot element with the starting position
    array = swap(array, start, pivot)
    pivot = start

    while(start < end):
        while start < len(array) and op(array[start], array[pivot]):
            start += 1

        # To encounter negative indexing, confirm strictly end is positive
        while end > 0 and not op(array[end], array[pivot]):
            end -= 1

        if start < end:
            array = swap(array, start, end)

    array = swap(array, end, pivot)
    return end


def sort(array: list, low: int, high: int, ascending: bool=True)-> list:
    op = get_operator(ascending)
    if high > low:
        part = partition(array, low, high, op)
        sort(array, low, part-1, op)
        sort(array, part+1, high, op)

    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Quick Sort (ascending):", sort(arr, 0, arr_size-1))
    print("Quick Sort (descending):", sort(arr, 0, arr_size-1, False))
