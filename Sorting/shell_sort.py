from typing import Iterator
from utils import get_operator, swap


def gap_sequence(size: int, method: str='shell')->Iterator[int]:
    """
    Utility for Shell Sort. Can be used to implement various strategy
    of finding next gaps

    Currently, only shell method is implemented, raises NotImplemented
    if any other method argumnet value is provided
    """
    if method == 'shell':
        k = 1
        while (gap := size // 2**k) > 1:
            yield gap
            k += 1
            gap = size // 2**k
    else:
        raise NotImplemented


def sort(array: list, size: int, ascending: bool=True, method: str='shell')-> list:
    op = get_operator(ascending)
    try:
        for gap in gap_sequence(size, method):
            for idx in range(0, size-gap):
                if op(array[idx+gap], array[idx]):
                    array = swap(array, idx, idx+gap)

                    # If swap happens then check with previous gap too
                    if idx-gap >= 0 and op(array[idx], array[idx-gap]):
                        array = swap(array, idx-gap, idx)
    except NotImplemented:
        print("Only shell method is implemented yet! Please skip method parameter for now.")
    return array

if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Shell Sort (ascending):", sort(arr, arr_size))
    print("Shell Sort (descending):",sort(arr, arr_size, False))
