# constant = 7
# for i in range(3, -1, -1):
#     k = constant - (2 * i)
#     print(f"{i * " "}{k * chr(68 - i)}{i * " "}")

for i in range(1, 5):
    for j in range(1, 6 - i):
        print(" ", end = " ")
    for j in range(1, i + 1):
        print(chr(j + 64), end=" ")
    for j in range(i - 1, 0, -1):
        print(chr(j + 64), end=" ")
    print("")