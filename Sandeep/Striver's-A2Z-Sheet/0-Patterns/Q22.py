for i in range(1, 8):
    for j in range(1, 8):
        if (i == 1 or i == 7 or j == 1 or j == 7):
            print(4, end=" ")
        else:
            if (i == 2 or i == 6 or j == 2 or j == 6):
                print(3, end=" ")
            else:
                if (i == 3 or i == 5 or j == 3 or j == 5):
                        print(2, end=" ")
                else:
                        print(1, end=" ")
                    
    print("")