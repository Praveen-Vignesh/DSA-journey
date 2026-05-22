def printsToN(currentNumber: int, maxTimes: int) -> None:
    """
    Recursively prints a number, until reached the maximum allowed number

    Args:
        currentNumber (int): The number that gets printed every iteration
        maxTimes (int): How many times do you want to print it

    Returns:
        None

    """

    if currentNumber == maxTimes + 1:
        return
    print(currentNumber)
    printsToN(currentNumber + 1, maxTimes)


printsToN(1, 5)
