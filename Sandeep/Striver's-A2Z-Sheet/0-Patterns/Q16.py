listOfStrings = []
for i in range(0, 5):
    listOfStrings += chr(i + 65)

for i in range(0, 5):
    print(" ".join(listOfStrings))
    listOfStrings.pop()