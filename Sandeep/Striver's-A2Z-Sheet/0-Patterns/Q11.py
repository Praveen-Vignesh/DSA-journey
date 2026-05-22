want = ""
for i in range(1, 6):
    if i % 2 != 0:
        want += str(1)
        print("".join(want))
    else:
        want += str(0)
        print("".join(want[::-1]))