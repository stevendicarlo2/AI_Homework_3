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
