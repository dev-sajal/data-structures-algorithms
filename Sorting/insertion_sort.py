from utils import get_operator


def sort(array: list, ascending: bool=True)-> list:
    """
    Idea:
    Mimick arrys having 2 part sorted and unsorted. Consider 1st element as sorted
    and start sorting from 2nd element. Pick the second element and find its place
    in the sorted list. This will maintain sorted list and grow it without messing
    up.
    Algorithm:
    Consider 1st element as sorted start from the next element
    Repeat i = 1..N-1
        Take key = A[i]
        Keep shifting elements to right, until right place of key is found at left.
        Fill key at the right place.
    done
    """
    op = get_operator(ascending)
    array_size = len(array)
    for i in range(1, array_size):
        key = array[i]
        j = i-1
        while(j>=0 and op(key, array[j])):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


if __name__ == '__main__':
    arr = list(range(10))
    arr.insert(4, 50)
    arr_size = len(arr)
    print("Initial Array: ", arr)

    print("--"*40)
    print("Insertion Sort (ascending):", sort(arr))
    print("Insertion Sort (descending):", sort(arr, False))
