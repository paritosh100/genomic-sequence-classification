import numpy as np


def viterbi(obs, states, start_p, trans_p, emit_p):
    n = len(obs)
    m = len(states)

    dp = np.zeros((m, n))
    path = np.zeros((m, n), dtype=int)

    # Initialization
    for i in range(m):
        dp[i][0] = start_p[i] * emit_p[i][obs[0]]

    # Recursion
    for t in range(1, n):
        for i in range(m):
            probabilities = [dp[j][t - 1] * trans_p[j][i] * emit_p[i][obs[t]] for j in range(m)]
            dp[i][t] = max(probabilities)
            path[i][t] = np.argmax(probabilities)

    # Backtracking
    best_path = [np.argmax(dp[:, n - 1])]
    for t in range(n - 1, 0, -1):
        best_path.insert(0, path[best_path[0]][t])

    return best_path


# Example Data
states = ['Coding', 'Non-Coding']
observations = [0, 1, 0, 2]  # Example nucleotide mapping
start_prob = [0.6, 0.4]
trans_prob = [[0.7, 0.3], [0.4, 0.6]]
emit_prob = [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]]

# Prediction
result = viterbi(observations, states, start_prob, trans_prob, emit_prob)
print("Predicted Sequence of States:", [states[i] for i in result])
