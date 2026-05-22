constant = 8
string = ""
for i in range(1, 5):
    string += str(i)
    k = constant - (2 * i)
    print(f"{string}{k * " "}{string}")