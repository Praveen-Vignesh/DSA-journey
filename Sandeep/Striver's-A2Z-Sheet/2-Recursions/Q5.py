def sumToN(toNumber: int) -> int:
    """
    Recursively sums First N Natural Numbers

    Args:
        toNumber (int): Upto what upper bound do you want to reach
    Returns:
        (int): the net sum
    """

    if toNumber == 1:
        return 1

    return toNumber + sumToN(toNumber - 1)

def sumToN_formula(toNumber: int) -> int:
    """
    Return the sum of first N Natural Numbers using formula

    Args:
        toNumber (int): Upto what upper bound do you want to reach
    Returns:
        (int): the net sum
    """
    return (toNumber * (toNumber + 1)) // 2

print(sumToN(5))
print("Now, using the formula...")
print(sumToN_formula(5))