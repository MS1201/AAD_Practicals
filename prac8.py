import streamlit as st

def lcs(P, Q):
    m = len(P)
    n = len(Q)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if P[i - 1] == Q[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if P[i - 1] == Q[j - 1]:
            lcs_sequence.append(P[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_sequence[::-1]  


st.title("Longest Common Subsequence Finder")


P = st.text_input("Enter first sequence (comma-separated):", "M,N,O,M")
Q = st.text_input("Enter second sequence (comma-separated):", "M,L,N,O,M")

if st.button("Find LCS"):
    P = P.split(',')
    Q = Q.split(',')
    result = lcs(P, Q)
    st.write("Longest Common Subsequence:", result)