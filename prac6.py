import streamlit as st

def matrix_chain_order(p):
    n = len(p) - 1 
    m = [[0] * n for _ in range(n)]  
    s = [[0] * n for _ in range(n)]  

    for l in range(2, n + 1):  
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf') 
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        return "(" + print_optimal_parens(s, i, s[i][j]) + print_optimal_parens(s, s[i][j] + 1, j) + ")"

st.title("Matrix Chain Multiplication")

input_dimensions = st.text_input("Enter matrix dimensions (comma-separated):", "5,10,3,12,5,50,6")

if st.button("Calculate"):
    try:
        dimensions = list(map(int, input_dimensions.split(',')))
        
        m, s = matrix_chain_order(dimensions)
        min_multiplications = m[0][len(dimensions) - 2]
        optimal_parenthesization = print_optimal_parens(s, 0, len(dimensions) - 2)

        st.write(f"Minimum number of multiplications is: {min_multiplications}")
        st.write(f"Optimal Parenthesization is: {optimal_parenthesization}")
    except Exception as e:
        st.error(f"Error: {e}")