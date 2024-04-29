import random

def print_board(board):
    for row in board:
        print('|'.join(row))
    print('-' * 5)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

def make_move(board, move, player):
    row, col = move
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)

    print("Let's play Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        move = (row, col)

        if move in available_moves(board):
            make_move(board, move, current_player)
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif len(available_moves(board)) == 0:
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == '__main__':
    play_game()
