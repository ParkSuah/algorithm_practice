def won(board, alph):
    # 상황으로 판단
    won = False
    for n in range(3):
        if board[n][0] == alph and board[n][1] == alph and board[n][2] == alph:
            return True
    
    for n in range(3):
        if board[0][n] == alph and board[1][n] == alph and board[2][n] == alph:
            return True
        
    if board[0][0] == alph and board[1][1] == alph and board[2][2] == alph:
        return True
    
    if board[0][2] == alph and board[1][1] == alph and board[2][0] == alph:
        return True
    
    return False

def solution(board):

    # 개수로 판단
    O_cnt = 0
    X_cnt = 0
    for row in board:
        O_cnt += row.count("O")
        X_cnt += row.count("X")
    if (X_cnt > O_cnt) or (O_cnt - X_cnt >= 2):
        return 0
    
    O_won = won(board, "O")
    X_won = won(board, "X")

    if O_won and X_won:
        return 0
    
    if O_won and (X_cnt >= O_cnt):
        return 0
    if X_won and (O_cnt > X_cnt):
        return 0
    return 1

        
        

    
test_case = [["OOX", "XXO", "OXO", 1], ["XXX", "XXX", "XXX", 0], ["OOO", "OOO", "OOO", 0], ["OXO", ".XO", "X.O", 1], ["OOO", "X.X", "...", 1], ["OOO", "...", "...", 0], ["O..", "...", "...", 1], [".O.", "...", "...", 1], ["..O", "...", "...", 1], ["...", "O..", "...", 1], ["...", ".O.", "...", 1], ["...", "..O", "...", 1], ["...", "...", "O..", 1], ["...", "...", ".O.", 1], ["...", "...", "..O", 1], ["X..", "...", "...", 0], [".X.", "...", "...", 0], ["..X", "...", "...", 0], ["...", "X..", "...", 0], ["...", ".X.", "...", 0], ["...", "..X", "...", 0], ["...", "...", "X..", 0], ["...", "...", ".X.", 0], ["...", "...", "..X", 0], ["OX.", ".OX", "..O", 1], ["O..", ".O.", "..O", 0], ["X..", ".X.", "..X", 0], ["XO.", "XO.", "XO.", 0], ["XO.", "...", "...", 1], ["OXO", "...", "...", 1], ["OXO", "X..", "...", 1], ["OXO", "XO.", "...", 1], ["OOO", "X.X", ".X.", 0], ["OOO", "X.X", "XX.", 0], ["XXX", "OO.", ".OO", 0], ["XO.", "OXO", "XOX", 1], ["OOO", "XOX", "XXO", 1], ["OOO", "OOX", "XXX", 0], ["XOX", "OXO", "XOX", 0], ["XXO", "OOX", "XO.", 1], ["XXO", "OOX", "XOO", 1], ["X.X", ".X.", "X.X", 0], [".X.", "X.X", ".X.", 0], ["O.O", ".O.", "O.O", 0], [".O.", "O.O", ".O.", 0], ["OX.", "OXO", ".XO", 0], ["OX.", "OX.", ".XO", 1], ["OX.", "OXO", "XXO", 1], ["OX.", "...", "...", 1], ["...", "...", "OX.", 1], ["OXO", "XOX", "OXO", 1], ["OOX", "XXO", "OOX", 1], ["XXX", ".OO", "O..", 1], ["OX.", ".O.", ".XO", 1], ["X.X", "X.O", "O.O", 1], ["XO.", "OXO", "XOX", 1], ["OOO", "XOX", "X.X", 0], ["XXX", "OO.", "OO.", 0], [".X.", "X..", ".O.", 0], ["XXX", "XOO", "OOO", 0], ["OOX", "OXO", "XOO", 0], ["OOX", "OXO", "XOX", 0], [".OX", "OXO", "XO.", 0], ["OOO", "XX.", "X..", 0]]

for t in test_case:
    answer = solution(t[:3])
    try:
        assert answer == t[3], f"***** {t[:3]} Fail."
    except:
        print(f"***** {t[:3]} Fail.")
    else:
        print(f"{t[:3]} Success.")
