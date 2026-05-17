hold = 0
for i in range(1, 6):
    list = []
    current = i
    while i > 0:
        hold += 1
        i -= 1
        list.append(str(hold))
        if len(list) == current:
            print(" ".join(list))