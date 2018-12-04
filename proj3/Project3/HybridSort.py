"""This module implements hybrid sorting"""

def insertion_sort(unsorted, reverse):
    """
    Sort the given list with insertion sort
    :param unsorted: the list to sort
    :param reverse: sort ascending if False, otherwise sort descending
    """
    def sort_predicate(left, right):
        if reverse:
            return left >= right
        return left <= right
    for i in range(0, len(unsorted) - 1):
        j = i + 1
        # insert unsorted[j] into the correct position in unsorted[0:j+1]
        to_insert = unsorted[j]
        # all unsorted[k] > unsorted[j] should be shifted over one
        k = j
        while k > 0:
            if sort_predicate(unsorted[k-1], to_insert):
                break
            unsorted[k] = unsorted[k-1]
            k -= 1
        # k is now the position where to_insert should be assigned
        # so that after assignment of to_insert, the following hold:
        #   for all n < k (unsorted[n] <= unsorted[k])
        #   and
        #   for all n > k (unsorted[n] > unsorted[k])
        unsorted[k] = to_insert
    return unsorted


def merge(first, second, reverse):
    """
    Merge the two sorted lists into a single list
    :param first: the first list
    :param second: the second list
    :param reverse: the lists are sorted ascending if False, descending if True
    """
    def sort_predicate(left, right):
        if reverse:
            return left > right
        return left < right
    len_first = len(first)
    len_second = len(second)
    i = 0
    j = 0
    merged = []
    while i < len_first and j < len_second:
        if sort_predicate(first[i], second[j]):
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    # Place remaining elements into merged
    # if i == len_first and j == len_second, then merged will be extended with
    # empty list
    if i == len_first:
        merged.extend(second[j:])
        return merged
    if j == len_second:
        merged.extend(first[i:])
        return merged


def partition(to_split):
    """
    Split the list into two halves
    :param to_split: the list to split
    """
    mid = len(to_split) // 2
    return (to_split[:mid], to_split[mid:])


def merge_sort(unsorted, threshold, reverse):
    """
    Sort a list using merge sort and insertion sort.
    If the length of the list is not greater than threshold then insertion
    sort is used.
    If threshold < 2 then the hybrid sort acts like a merge sort
    If threshold >= 2 then insertion sort will be used for some recursive call
    of merge sort.
    :param unsorted: the list to sort
    :param threshold: the point at which to use insertion rather than merge sort
    :param reverse: sort in ascending order if False, otherwise sort descending
    """
    if len(unsorted) <= 1:
        return unsorted
    if len(unsorted) <= threshold:
        unsorted = insertion_sort(unsorted, reverse)
    else:
        left_half, right_half = partition(unsorted)
        left_half = merge_sort(left_half, threshold, reverse)
        right_half = merge_sort(right_half, threshold, reverse)
        unsorted = merge(left_half, right_half, reverse)
    return unsorted
