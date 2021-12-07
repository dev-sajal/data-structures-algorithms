from utils import get_operator, swap


def sort(array: list, ascending: bool=True)-> list:
    """
    Idea:
    Sort the arrays by bubbling the largest (in ascending) element in each pass
    to the last.
    """
    op = get_operator(ascending)
    array_size = len(array)
    for i in range(array_size-1):
        for j in range(i+1, array_size):
            if op(array[j], array[i]):
                array = swap(array, i, j)

    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Bubble Sort (ascending):", sort(arr))
    print("Bubble Sort (descending):", sort(arr, False))
