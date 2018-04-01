TEAM_NAME = "team"
MEMBERS = ["snd7nb","yq4du"]

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

def get_column_move(board, n, token):
    return 2

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

def winnning_moves(board, n, token):
    moves = []
    for col in range(len(board)):
        if is_winning_move(board, n, col, token):
            moves.append(col)
    return moves

def losing_moves(board, n, token):
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
        ["R","R"],
        ["Y"],
        ["R","Y"],
        ["Y","Y"],
        ["Y"],
    ]
}
print(losing_moves(sample_state["board"], 3, "Y"))
