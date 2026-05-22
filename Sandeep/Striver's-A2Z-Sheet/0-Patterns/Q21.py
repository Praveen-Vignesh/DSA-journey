stars = int(input())
for i in range(0, stars):
    constant = stars - 2
    if i == 0 or i == stars - 1:
        print(stars * "*")
    else:
        print(f"*{constant * " "}*")