string = []
for i in range(0, 5):
    string += chr(i + 65)

for i in range(0, 5):
    print(" ".join(string))
    string.pop()