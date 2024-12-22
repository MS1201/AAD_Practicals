import time
import streamlit as st
import plotly.graph_objects as go

# Loop Method
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Equation Method
def sum_equation(n):
    return (n * (n + 1)) // 2

# Recursion Method
def sum_recursion(n):
    if n <= 1:
        return n
    return n + sum_recursion(n - 1)

# Timing Function
def time_function(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

# Streamlit App
def main():
    st.title('Sum Calculation Performance Comparison')

    # User input for N
    n = st.number_input('Enter a value for N:', min_value=1, value=100)

    # Time calculations
    time_loop = time_function(sum_loop, n)
    time_equation = time_function(sum_equation, n)
    time_recursion = time_function(sum_recursion, n)

    # Display results
    st.write(f"Time taken by loop method: {time_loop:.6f} seconds")
    st.write(f"Time taken by equation method: {time_equation:.6f} seconds")
    st.write(f"Time taken by recursion method: {time_recursion:.6f} seconds")

    # Plot
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=['Loop', 'Equation', 'Recursion'],
        y=[time_loop, time_equation, time_recursion],
        name='Execution Time'
    ))

    fig.update_layout(
        title='Comparison of Execution Times',
        xaxis_title='Method',
        yaxis_title='Time (seconds)',
    )

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
