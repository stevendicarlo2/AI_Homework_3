TEAM_NAME = "team"
MEMBERS = ["snd7nb","yq4du"]

import random

def get_move(state):
    cols = state["columns"]
    n = state["connect_n"]
    token = state["your-token"]
    board = state["board"]

    column_to_play = get_column_move(board, n, token)
    team_code = state["team-code"]
    return {
        "move": column_to_play,
        "team-code": team_code
    }

# Win if possible. Otherwise, block opponent if possible. Otherwise, play move that will not lead to winning
# opportunity for opponent, and won't take away a dangerous spot for opponent. If none of that is possible, just play
# a random move.
def get_column_move(board, n, token):
    winning_moves = get_winning_moves(board, n, token)
    if len(winning_moves) > 0:
        return winning_moves[0]

    opp_token = "R" if token == "Y" else "Y"
    blocking_moves = get_winning_moves(board, n, opp_token)
    if len(blocking_moves) > 0:
        return blocking_moves[0]

    losing_moves = get_losing_moves(board, n, token)
    opp_losing_moves = get_losing_moves(board, n, opp_token)
    move_list = []
    for col in range(len(board)):
        if col not in losing_moves and col not in opp_losing_moves:
            move_list.append(col)

    if len(move_list) > 0:
        return random.choice(move_list)
    elif len(opp_losing_moves) > 0:
        return random.choice(opp_losing_moves)
    else:
        return random.choice([i for i in range(len(board))])

def vertical_win(board, n, column, token):
    can_be_winning_move = True
    if n-1 > len(board[column]):
        return False
    for i in range(1, n, 1):
        if board[column][-i] != token:
            can_be_winning_move = False
    return can_be_winning_move


def get_chip_or_none(board, column, index):
    if column < 0 or column > len(board)-1:
        return None
    if index < 0 or index > len(board[column])-1:
        return None
    return board[column][index]

def horizontal_win(board, n, column, token):
    if n > len(board):
        return False
    row = len(board[column])
    length = 1
    disp = -1
    chip = get_chip_or_none(board, column + disp, row)
    while chip == token:
        disp -= 1
        chip = get_chip_or_none(board, column + disp, row)
        length += 1
    disp = 1
    chip = get_chip_or_none(board, column + disp, row)
    while chip == token:
        disp += 1
        chip = get_chip_or_none(board, column + disp, row)
        length += 1
    return length >= n

def diagonal_win1(board, n, column, token):
    if n > len(board):
        return False
    row = len(board[column])
    length = 1
    disp = -1
    chip = get_chip_or_none(board, column + disp, row + disp)
    while chip == token:
        disp -= 1
        chip = get_chip_or_none(board, column + disp, row + disp)
        length += 1
    disp = 1
    chip = get_chip_or_none(board, column + disp, row + disp)
    while chip == token:
        disp += 1
        chip = get_chip_or_none(board, column + disp, row + disp)
        length += 1
    return length >= n

def diagonal_win2(board, n, column, token):
    if n > len(board):
        return False
    row = len(board[column])
    length = 1
    disp = -1
    chip = get_chip_or_none(board, column + disp, row - disp)
    while chip == token:
        disp -= 1
        chip = get_chip_or_none(board, column + disp, row - disp)
        length += 1
    disp = 1
    chip = get_chip_or_none(board, column + disp, row - disp)
    while chip == token:
        disp += 1
        chip = get_chip_or_none(board, column + disp, row - disp)
        length += 1
    return length >= n

def is_winning_move(board, n, column, token):
    return (vertical_win(board, n, column, token) or
            horizontal_win(board, n, column, token) or
            diagonal_win1(board, n, column, token) or
            diagonal_win2(board, n, column, token))

def get_winning_moves(board, n, token):
    moves = []
    for col in range(len(board)):
        if is_winning_move(board, n, col, token):
            moves.append(col)
    return moves

def get_losing_moves(board, n, token):
    temp_board = deep_copy(board)
    opp_token = "R" if token == "Y" else "Y"
    moves = []
    for col in range(len(temp_board)):
        temp_board[col].append(token)
        if col > 0:
            del temp_board[col-1][-1]
        if is_winning_move(temp_board, n, col, opp_token):
            moves.append(col)
    return moves

def deep_copy(board):
    copy = [[board[x][y] for y in range(len(board[x]))] for x in range(len(board))]
    return copy

sample_state = {
    "team-code": "eef8976e",
    "game": "connect_more",
    "opponent-name": "mighty_ducks",
    "columns": 6,
    "connect_n": 5,
    "your-token": "R",
    "board": [
        ["R","Y"],
        ["Y","R"],
        ["Y"],
    ]
}
board = sample_state["board"]
print(get_column_move(board, 3, "R"))
