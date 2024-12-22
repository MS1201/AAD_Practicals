import streamlit as st

def knapsack(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Streamlit UI
st.title("Knapsack Problem Solver")

# Input values
n = 4
W = 5
values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]

st.write("Artefacts Values:", values)
st.write("Artefacts Weights:", weights)
st.write("Knapsack Capacity:", W)

# Calculate maximum value
max_value = knapsack(values, weights, W)
st.write("Maximum value that can be stolen:", max_value)