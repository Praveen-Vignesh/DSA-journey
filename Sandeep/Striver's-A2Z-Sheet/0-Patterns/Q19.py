for i in range(0, 5):
    k = 5 - (i)
    joins = k * "*"
    print(f"{joins}{2 * i * " "}{(joins)}")
constant = 10
for i in range(1, 6):
    k = constant - (2 * i)
    print(f"{i * "*"}{k * " "}{i * "*"}")