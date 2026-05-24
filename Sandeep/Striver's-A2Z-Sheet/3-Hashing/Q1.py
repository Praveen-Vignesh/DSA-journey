#
# Problem Statement:
# Given an array, we have found the number of occurrences of each element in the array.

from collections import defaultdict, Counter
from typing import List


def countFrequency_hashtable(array: List[int]) -> dict:
    """
    Uses the built-in defaultdict() datatype from `collections` module

    Args:
        array (List(int)): the array whose counts we want to measure

    Returns:
        dict: the dict() of the counts
    """
    # define the hashtable
    frequency = defaultdict(int)
    # pre-compute step
    for element in array:
        frequency[element] += 1

    return dict(frequency)


def countFrequency_pythonic(array: List[int]) -> dict:
    """
    Uses the built-in Counter() method to count instances, from `collections` module

    Args:
        array (List(int)): the array whose counts we want to measure

    Returns:
        dict: the dict() of the counts
    """

    # Pre-compute
    frequency = Counter(array)
    return dict(frequency)


array = [10, 5, 10, 15, 10, 5]
print(countFrequency_hashtable(array=array))
