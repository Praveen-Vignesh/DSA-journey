from collections import defaultdict, Counter
from typing import List, Tuple


def mostLeast_hashtable(array: List[int]) -> Tuple[List[int], List[int]]:
    """
    Finds the most occuring and least occuring elements from the given array, using defaultdict()

    Args:
        array (List(int)): the array whose counts we want to measure

    Returns:
        Tuple(int, int): First place is the highest occuring element, and second place is the lowest occuring element
    """
    if not array:
        return [], []

    # define the hashtable
    frequency = defaultdict(int)
    # pre-compute step
    for element in array:
        frequency[element] += 1

    most_occurrences = max(frequency.values())
    mostOccuringValues = [k for k, v in frequency.items() if v == most_occurrences]
    least_occurrences = min(frequency.values())
    leastOccuringValues = [k for k, v in frequency.items() if v == least_occurrences]

    return mostOccuringValues, leastOccuringValues


def mostLeast_Pythonic(array: List[int]) -> Tuple[List[int], List[int]]:
    """
    Finds the most occuring and least occuring elements from the given array, using Counter()

    Args:
        array (List(int)): the array whose counts we want to measure

    Returns:
        Tuple(int, int): First place is the highest occuring element, and second place is the lowest occuring element
    """
    if not array:
        return [], []

    frequency = Counter(array)
    most_occurrences = max(frequency.values())
    mostOccuringValues = [k for k, v in frequency.items() if v == most_occurrences]
    least_occurrences = min(frequency.values())
    leastOccuringValues = [k for k, v in frequency.items() if v == least_occurrences]

    return mostOccuringValues, leastOccuringValues

