import streamlit as st
import time
import matplotlib.pyplot as plt

def fibonacci_iterative(n):
    if n <= 0:
        return 0, 1
    elif n == 1:
        return 1, 2
    
    a, b = 1, 1
    steps = 3
    for _ in range(2, n):
        a, b = b, a + b
        steps += 1
    return b, steps

def fibonacci_recursive(n, steps=1):
    if n <= 0:
        return 0, steps
    elif n == 1 or n == 2:
        return 1, steps + 1
    else:
        fib1, steps1 = fibonacci_recursive(n - 1, steps + 1)
        fib2, steps2 = fibonacci_recursive(n - 2, steps1 + 1)
        return fib1 + fib2, steps2 + 1

def measure_performance(func, n):
    start_time = time.time()
    result, steps = func(n)
    end_time = time.time()
    return result, steps, end_time - start_time

st.title("Fibonacci Rabbit Problem")

n = st.number_input("Enter the number of months:", min_value=1, max_value=35, value=12, step=1)

if st.button("Calculate"):
    iterative_result, iterative_steps, iterative_time = measure_performance(fibonacci_iterative, n)
    recursive_result, recursive_steps, recursive_time = measure_performance(fibonacci_recursive, n)

    st.write(f"Number of rabbit pairs after {n} months:")
    st.write(f"Iterative method: {iterative_result}")
    st.write(f"Recursive method: {recursive_result}")

    st.write("\nPerformance comparison:")
    st.write(f"Iterative method: {iterative_steps} steps, {iterative_time:.6f} seconds")
    st.write(f"Recursive method: {recursive_steps} steps, {recursive_time:.6f} seconds")

    
    months = list(range(1, n + 1))
    iterative_times = [measure_performance(fibonacci_iterative, i)[2] for i in months]
    recursive_times = [measure_performance(fibonacci_recursive, i)[2] for i in months]

    fig1, ax1 = plt.subplots()
    ax1.plot(months, iterative_times, label="Iterative")
    ax1.plot(months, recursive_times, label="Recursive")
    ax1.set_xlabel("Number of months")
    ax1.set_ylabel("Execution time (seconds)")
    ax1.set_title("Time Comparison: Iterative vs Recursive")
    ax1.legend()

    st.pyplot(fig1)

    iterative_steps = [measure_performance(fibonacci_iterative, i)[1] for i in months]
    recursive_steps = [measure_performance(fibonacci_recursive, i)[1] for i in months]

    fig2, ax2 = plt.subplots()
    ax2.plot(months, iterative_steps, label="Iterative")
    ax2.plot(months, recursive_steps, label="Recursive")
    ax2.set_xlabel("Number of months")
    ax2.set_ylabel("Number of steps")
    ax2.set_title("Step Count Comparison: Iterative vs Recursive")
    ax2.legend()

    st.pyplot(fig2)

