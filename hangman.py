def hangman(word):
    wrong = 0
    stages = ["",
              "____     ",
              "|        ",
              "|    |   ",
              "|    0   ",
              "|   /|\  ",
              "|   / \  ",
              "|        ",
              ]
    rletters = list(word)
    board [""] * len(word)
    win = False
    print("welcome to hangman")
    

    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            rletters[cind] = "$"
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".stages[0:e])
            if _ not in board:
                print("you are the winner")
                print("".join(board))
                win = True
                break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("you are lose! the answer is {}.format(word)")
    hangman("cat")
