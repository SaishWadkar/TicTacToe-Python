# create lists of list

def check(board,p1,p2):

    # all positions full tie
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return ("0","Tie")

    # 1 horizontal p1
    elif board[0][0] == board[0][1] ==board[0][2] == p1 \
            or board[1][0] == board[1][1] ==board[1][2] ==p1 \
            or board[2][0] == board[2][1] ==board[2][2] ==p1 :
        return ("0","Player 1 WON by horizontal")

    # horizontal p2
    elif board[0][0] == board[0][1] ==board[0][2] == p2 \
            or board[1][0] == board[1][1] ==board[1][2] ==p2 \
            or board[2][0] == board[2][1] ==board[2][2] ==p2 :
        return ("0","Player 2 WON by horizontal")

    # 2 vertical p1
    elif board[0][0] == board[1][0] ==board[2][0] == p1 \
            or board[0][1] == board[1][1] ==board[2][1] == p1 \
            or board[0][2] == board[1][2] ==board[2][2] == p1:
        return ("0","Player 1 WON by vertical")

    # 2 vertical p2
    elif board[0][0] == board[1][0] ==board[2][0] == p2 \
            or board[0][1] == board[1][1] ==board[2][1] == p2 \
            or board[0][2] == board[1][2] ==board[2][2] == p2:
        return ("0","Player 2 WON by vertical")

    # 3 diagonal 1 p1
    elif board[0][0]==board[1][1]==board[2][2]==p1 :
        return ("0","Player 1 won by (forward) diagonal")

    # diagonal 1 p2
    elif board[0][0] == board[1][1] == board[2][2] == p2:
        return ("0", "Player 2 won by (forward) diagonal")

    # 4 diagonal 2 p1
    elif board[0][2]==board[1][1]==board[2][0]==p1 :
        return ("0","Player 1 won by (backward) diagonal")

    # diagonal 2 p2
    elif board[0][2] == board[1][1] == board[2][0] == p2:
        return ("0", "Player 2 won by (backward) diagonal")

    else:
        return ("1","")


