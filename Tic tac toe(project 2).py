def print_board(board):
    for row in board:
        print("    |  ".join(row))

        print("-----" * 4)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def minimax(board, depth, is_maximizing):
    if check_winner(board, ' X'):
        return -10
    if check_winner(board, 'O'):
        return 10
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_maximizing) - depth)
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ' X'
                    best = min(best, minimax(board, depth + 1, not is_maximizing) + depth)
                    board[i][j] = ' '
        return best

def ai_move(board):
    best_score = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turns = 0

    while turns < 9:
        print_board(board)

        if turns % 2 == 0:
            print("Your turn (X)")

            while True:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again!")

            board[row][col] = ' X'
        else:
            print("AI's turn (O)")
            row, col = ai_move(board)
            board[row][col] = 'O'

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            return
        elif check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            return

        turns += 1

    print_board(board)
    print("Match draw!")

if __name__== "__main__":
    main()