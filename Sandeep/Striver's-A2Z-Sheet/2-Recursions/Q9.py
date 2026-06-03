from typing import List


def fibonacciSequence(endNumber: int) -> List[int]:
    """
    Generates the entire fibonacci sequence upto a certain number

    Args:
        endNumber (int): The final number while to make out of this generator
    Returns:
        List[int]: The sequence neatly packed inside a list
    """
    sequence = [1, 1]
    for value in range(2, endNumber):
        nextValue = sequence[-1] + sequence[-2]
        sequence.append(nextValue)
    return sequence


def fibonacci_recursive(endNumber: int) -> int:
    """
    Return the final number in the fibonacci sequence upto a certain number of steps

    Args:
        endNumber (int): The number of steps allowed to take
    Returns:
        int: The final number
    """
    if endNumber <= 1:
        return endNumber
    return fibonacci_recursive(endNumber - 1) + fibonacci_recursive(endNumber - 2)


print(f"The entire sequence is = {fibonacciSequence(endNumber=3)}")
print(f"The final number in the sequence is = {fibonacci_recursive(endNumber=3)}")
