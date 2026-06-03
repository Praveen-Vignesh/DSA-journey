listOfNumbers = [str(i) for i in range(1, 6)]
for i in range(1, 6):
    print("".join(listOfNumbers))
    listOfNumbers.pop()