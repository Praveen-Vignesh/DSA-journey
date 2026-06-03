def factorial_ofN(toNumber: int) -> int:
    """
    Recursively calculates the factorial upto the first N Natural Numbers

    Args:
        toNumber (int): Upto what upper bound do you want to reach
    Returns:
        (int): the final factorial
    
    """
    if toNumber == 0:
        return 1

    return toNumber * factorial_ofN(toNumber - 1)

print(factorial_ofN(5))
