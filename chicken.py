TEAM_NAME = "team"
MEMBERS = ["snd7nb","yq4du"]

def get_move(state):
    prior_info = load_data()
    prior_info["past_reaction_times"].append(state["prev-response-time"])

    opponent_name = state["opponent-name"]
    if opponent_name not in prior_info["past_results"]:
        prior_info["past_results"][opponent_name] = []

    last_opponent = prior_info["last_opponent"]
    last_submitted_time = prior_info["last_submitted_time"]
    last_opponent_play = state["last-opponent-play"]
    last_outcome = state["last-outcome"]
    prior_info["past_results"][last_opponent].append((last_submitted_time, last_opponent_play, last_outcome))

    time_to_play = get_time(prior_info)
    prior_info["last_submitted_time"] = time_to_play
    prior_info["last_opponent"] = opponent_name
    save_data(prior_info)

    team_code = state["team-code"]
    return {
        "move": time_to_play,
        "team-code": team_code
    }

def get_time(prior_info):
    return .2

def load_data():
    sample_info = {
        "past_reaction_times": [.1, .12, .32],
        "past_results": {
            "opponent1": [(.1, .2, "crash"), (.1, .1, "tie"), (.2, .1, "win")],
            "opponent2": [(.3, .3, "tie")]
        },
        "last_opponent": "opponent2",
        "last_submitted_time": .2
    }
    return sample_info

def save_data(info):
    return
