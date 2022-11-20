if __name__ == "__main__":
    hold = 0
    lock = 0
    print("R,Y,G,B,M,W")
    words = input("Words: ")
    colrs = input("Color of Words: ")
    if colrs[7] == "R":
        if words.count("G") >= 3:
            c = 0
            while (hold <= 2) or (c > 7):
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
            if (words[7 - c] == "W") or (colrs[7 - c] == "W"):
                print("YES on word #" + str(8 - c))
                exit()
    if colrs[7] == "Y":
        for c in range(0, 8):
            if (colrs[c] == "G") and (words[c] == "B"):
                lock = 1
        if lock == 1:
            print("YES on word #" + str(colrs.index("G") + 1))
            exit()
        lock = 0
        for c in range(0, 8):
            if ((colrs[c] == "W") or (colrs[c] == "R")) and (words[c] == "W"):
                lock = 1
        hold = 0
        if lock == 1:
            for c in range(0, 8):
                if not (colrs[c] == words[c]):
                    if hold == 1:
                        print("YES on word #" + str(c + 1))
                        exit()
                    if hold == 0:
                        hold = 1
        hold = 0
        for c in range(0, 8):
            if (colrs[c] == "M") or (words[c] == "M"):
                hold = hold + 1
        print("NO on word #" + str(hold))
        exit()
    if colrs[7] == "G":
        for c in range(0, 7):
            if (words[c] == words[c + 1]) and not (colrs[c] == colrs[c + 1]):
                print("NO on word #5")
                exit()
        if words.count("M") >= 3:
            for c in range(0, 8):
                if (colrs[c] == "Y") or (words[c] == "Y"):
                    print("NO on word #" + str(c + 1))
                    exit()
        for c in range(0, 8):
            if colrs[c] == words[c]:
                print("YES on word #" + str(c + 1))
                exit()
    if colrs[7] == "B":
        for c in range(0, 8):
            if not (colrs[c] == words[c]):
                hold = hold + 1
        if hold >= 3:
            for c in range(0, 8):
                if not (colrs[c] == words[c]):
                    print("YES on word #" + str(c + 1))
                    exit()
        for c in range(0, 8):
            if (words[c] == "R" and colrs[c] == "Y") or (words[c] == "Y" and colrs[c] == "W"):
                for c1 in range(0, 8):
                    if (words[c1] == "W") and (colrs[c1] == "R"):
                        print("NO on word #" + str(c1 + 1))
                        exit()
        for c in range(0, 8):
            if (colrs[7 - c] == "G") or (words[7 - c] == "G"):
                print("YES on word #" + str(8 - c))
                exit()
    if colrs[7] == "M":
        for c in range(0, 7):
            if (colrs[c] == colrs[c + 1]) and not (words[c] == words[c + 1]):
                print("YES on word #3")
                exit()
        if words.count("Y") > colrs.count("B"):
            for c in range(0, 8):
                if words[7 - c] == "Y":
                    print("NO on word #" + str(8 - c))
                    exit()
        for c in range(0, 8):
            if colrs[c] == words[6]:
                print("NO on word #" + str(c + 1))
                exit()
    if colrs[7] == "W":
        if (colrs[2] == words[3]) or (colrs[2] == words[4]):
            for c in range(0, 8):
                if (colrs[c] == "B") or (words[c] == "B"):
                    print("NO on word #" + str(c + 1))
                    exit()
        for c in range(0, 8):
            if (colrs[c] == "R") and (words[c] == "Y"):
                for c1 in range(0, 8):
                    if colrs[7 - c1] == "B":
                        print("YES on word #" + str(8 - c1))
                        exit()
        print("NO on any word")

    print("wrong format or code broken")
