from typing import List


## we are keeping the best method first
def reverseAString_twoPointers(array: List[str]) -> List[str]:
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


def isPalindrome_twoPointer(string: str) -> bool:
    """
    Uses the 2 pointer method to compare if the given string is a palindrome or not

    Args:
        string (str): The string we want to check
    Returns:
        bool: The verdict

    """


    return list(string) == reverseAString_twoPointers(list(string))


def isPalindrome_recursion(string: str, currentPlace: int = 0) -> bool:
    """
    Recursively runs through the string, the entire string is cut into 2 parts. 
    The left part and the right part, and then we compare similarly to 2 pointers method, 
    we move ahead if both pointers on both of the parts are same, else it's not a palindrome 
    until the both parts are not exhausted.

    Args:
        string (str): The string we want to compare
        currentPlace (int): The current place of the pointer, Default value = 0th place
    
    Returns:
        bool: is the input string a palindrome or not
    """
    if currentPlace >= len(string) // 2:
        return True

    if string[currentPlace] != string[len(string) - currentPlace - 1]:
        return False

    return isPalindrome_recursion(string, currentPlace + 1)


inputString = "madam"
print(
    f"Is {inputString} a palidrome (using Twopointer method)?: {isPalindrome_twoPointer(inputString)}"
)
print(
    f"Is {inputString} a palidrome (using recurssion method)?: {isPalindrome_recursion(inputString)}"
)
