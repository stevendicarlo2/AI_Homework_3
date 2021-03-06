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

def get_upper_prediction_bound(data):
    n = len(data)
    avg = sum(data)/n
    temp = 0
    for point in data:
        temp += (point-avg)**2
    var = temp/(n-1)
    stddev = var**(1/2)
    t_table_90 = [3.08,
                  1.89,
                  1.64,
                  1.53,
                  1.48,
                  1.44,
                  1.42,
                  1.4,
                  1.38,
                  1.37,
                  1.36,
                  1.36,
                  1.35,
                  1.35,
                  1.34,
                  1.34,
                  1.33,
                  1.33,
                  1.33,
                  1.33,
                  1.32,
                  1.32,
                  1.32,
                  1.32,
                  1.32,
                  1.32,
                  1.31,
                  1.31,
                  1.31,
                  1.31]
    t_score = 1.28 if n > 31 else t_table_90[n-2]
    prediction_upper_bound = avg + t_score*stddev*(1+1/n)**(1/2)
    return prediction_upper_bound

def load_data():
    sample_info = {
        "past_reaction_times": [.1, .12, .32],
        "past_results": {
            "opponent1": [(.1, .2, -10), (.1, .1, 0), (.2, .1, -1)],
            "opponent2": [(.3, .3, 0)]
        },
        "last_opponent": "opponent2",
        "last_submitted_time": .2
    }
    return sample_info

def save_data(info):
    return

sample_data = [0, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 3]
print(get_upper_prediction_bound(sample_data))
