def printsToN_backwards(fromNumber: int, toNumber: int) -> None:
    """
    Recursively prints the upper limit, until reached the lower limit

    Args:
        fromNumber (int): Lower bound (or limit)
        toNumber (int): Upper bound (or limit)

    Returns:
        None

    """

    if fromNumber == toNumber + 1:
        return
    print(toNumber)
    printsToN_backwards(fromNumber, toNumber - 1)


printsToN_backwards(100, 105)
