constant = 9
for i in range(4, -1, -1):
    k = constant - (2 * i)
    print(f"{i * ' ' }{(k * '*')}{i * ' '}")