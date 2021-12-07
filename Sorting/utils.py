from operator import ge, le


def get_operator(ascending: bool)-> callable:
    """ Less than equal operator for ascending operator,
     else greater than equal """
    return le if ascending else ge


def swap(array, i, j):
    """ Function for swapping array indexes """
    array[i], array[j] = array[j], array[i]
    return array


def find_max_index(array: list)->int:
    argmax = 0
    for idx, element in enumerate(array):
        if ge(element, array[argmax]):
            argmax = idx

    return argmax


def find_min_index(array: list)->int:
    argmin = 0
    for idx, element in enumerate(array):
        if le(element, array[argmin]):
            argmin = idx

    return argmin
