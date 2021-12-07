from utils import find_max_index, find_min_index


def sort(array: list, size: int, n_buckets: int, ascending: bool=True)->list:
    max_element = array[find_max_index(array)]
    min_element = array[find_min_index(array)]

    elements_range = (max_element - min_element)/n_buckets
    buckets = []

    buckets = [[] for _ in range(n_buckets)]
    for element in array:
        index = (element - min_element)/elements_range
        integer_part = index - int(index)

        if integer_part == 0 and element != min_element:
            buckets[int(index)-1].append(element)
        else:
            buckets[int(index)].append(element)


    for bucket in buckets:
        if bucket:
            bucket.sort()

    array = []
    if ascending:
        for bucket in range(n_buckets):
            if buckets[bucket]:
                array.extend(buckets[bucket])
    else:
        for bucket in range(n_buckets-1, -1, -1):
            if buckets[bucket]:
                array.extend(buckets[bucket][::-1])

    return array


def sort_mixed(array: list, size: int, n_buckets: int, ascending: bool=True)->list:
    """
    Uses bucket sort when both negative and positive are present
    """
    negative = []
    positive = []
    for element in array:
        if element < 0:
            negative.append(-1*element)
        else:
            positive.append(element)

    negative = sort(negative, len(negative), n_buckets)
    positive = sort(positive, len(positive), n_buckets)

    array = []
    if ascending:
        for idx in range(len(negative)-1, -1, -1):
            array.append(negative[idx] * -1)

        for element in positive:
            array.append(element)
    else:
        for element in positive:
            array.append(element)

        for element in negative:
            array.append(element * -1)

    return array



if __name__ == '__main__':
    arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
    arr_size = len(arr)
    print("Bucket sort (ascending):", sort(arr, arr_size, 5))
    print("Bucket sort (descending):", sort(arr, arr_size, 5, False))
