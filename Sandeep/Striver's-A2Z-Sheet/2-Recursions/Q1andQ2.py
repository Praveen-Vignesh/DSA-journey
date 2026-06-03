def printsNTimes(someString: str, times: int) -> None:
    """
    Recursively prints a certain word a number of time

    Args:
        someString (str): The string you want to print
        times (int): How many times do you want to print it

    Returns:
        None

    """
    global counter
    if times == 0:
        return
    print(someString)
    printsNTimes(someString, times - 1)


printsNTimes("Wow", 5)
