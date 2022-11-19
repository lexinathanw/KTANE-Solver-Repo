if __name__ == "__main__":
    hold = 0
    lock = 0
    print("R,Y,G,B,M,W")
    words = input("Words: ")
    colrs = input("Color of Words: ")
    if colrs[7] == "R":
        if words.count("G") >= 3:
            c = 0
            while hold <= 2 or c > 7:
                if words[c] == "G":
                    hold = hold + 1
                elif colrs[c] == "G":
                    hold = hold + 1
                c = c + 1
            if hold > 2:
                print("YES on word #" + str(c))
                exit()
        if colrs.count("B") == 1:
            print("NO on word #" + str(words.index("M") + 1))
            exit()
        for c in range(0, 8):
            if words[7 - c] == "W" or colrs[7 - c] == "W":
                print("YES on word #" + str(8 - c))
                exit()
    if colrs[7] == "Y":
        for c in range(0, 8):
            if colrs[c] == "G" and words[c] == "B":
                lock = 1
        if lock == 1:
            print("YES on word #" + str(colrs.index("G")+1))
            exit()
        lock = 0
        for c in range(0, 8):
            if (colrs[c] == "W" or colrs[c] == "R") and words[c] == "W":
                lock = 1
        hold = 0
        if lock == 1:
            for c in range(0, 8):
                if not(colrs[c] == words[c]):
                    if hold == 0:
                        hold = 1
                    if hold == 1:
                        print("YES on word #" + str(c+1))
        hold = 0
        for c in range(0, 8):
            if colrs[c] == "M" or words[c] == "M":
                hold = hold + 1
        print("NO on word #" + str(hold))
    else:
        print("code incomplete")
