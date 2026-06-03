from typing import List


def reverseAnArray_pythonic(array: List[int]) -> List[int]:
    """
    Reverses an array using Python dependent technique

    Args:
        array (List[int]): The array of integers we want to reverse
    Returns:
        List[int]: reversed array

    """
    return array[::-1]


def reverseAnArray_twoArrays(array: List[int]) -> List[int]:
    """
    Reverses an array using another array

    Args:
        array (List[int]): The array of integers we want to reverse
    Returns:
        List[int]: reversed array

    """
    n = len(array)
    returnArray = [0] * n
    for place in range(n):
        returnArray[place] = array[n - 1 - place]
    return returnArray


def reverseAnArray_twoPointers(array: List[int]) -> List[int]:
    """
    Reverses an array using 2 pointers, pointing at the start and end of the array
    they cross for the loop to stop running, that's when we know the original array
    has been reversed in place

    Args:
        array (List[int]): The array of integers we want to reverse
    Returns:
        List[int]: reversed array

    """

    right = len(array) - 1
    left = 0
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array


nums = [1, 2, 3, 4, 5, 6]
print("Pythonic way of doing it...\n", reverseAnArray_pythonic(nums))
print("Using 2 seperate arrays...\n", reverseAnArray_twoArrays(nums))
print(
    "Using 2 pointer method to swap elements...\n",
    reverseAnArray_twoPointers(nums),
)
