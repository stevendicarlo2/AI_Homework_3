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

def get_normal_confidence_bound(data):
    n = len(data)
    avg = sum(data)/n
    temp = 0
    for point in data:
        temp += (point-avg)**2
    var = temp/(n-1)

    chi2_table_90 = [2.706,
                     4.605,
                     6.251,
                     7.779,
                     9.236,
                     10.645,
                     12.017,
                     13.362,
                     14.684,
                     15.987,
                     17.275,
                     18.549,
                     19.812,
                     21.064,
                     22.307,
                     23.542,
                     24.769,
                     25.989,
                     27.204,
                     28.412]
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
    sample_n = min(n, 30)
    z_score = 1.28 if n > 31 else t_table_90[n-2]
    var_upper_bound = var + (sample_n-1)*var/chi2_table_90[sample_n-2]
    stddev_upper_bound = var_upper_bound**.5
    mean_upper_bound = avg + z_score*((var/n)**.5)
    return mean_upper_bound, stddev_upper_bound

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

sample_data = [0, 1, 2, 3]
print(get_normal_confidence_bound(sample_data))
