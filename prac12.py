import streamlit as st
import numpy as np
from itertools import permutations

def calculate_min_cost_path(distance_matrix):
    n = len(distance_matrix)
    min_cost = float('inf')
    min_path = []

    for perm in permutations(range(n)):
        current_cost = 0
        for i in range(n):
            current_cost += distance_matrix[perm[i]][perm[(i + 1) % n]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = perm

    return min_path, min_cost

st.title("Traveling Salesman Problem Solver")

input_matrix = st.text_area("Enter the distance matrix (as a list of lists):", 
                             value='[[float("inf"), 20, 30, 10, 11], [15, float("inf"), 16, 4, 2], [3, 5, float("inf"), 2, 4], [19, 6, 18, float("inf"), 3], [16, 4, 7, 16, float("inf")]]')

try:
    distance_matrix = eval(input_matrix)
    distance_matrix = np.array(distance_matrix)
    
    if st.button("Calculate Minimum Path"):
        min_path, min_cost = calculate_min_cost_path(distance_matrix)
        
        st.write("Minimum Path:")
        for i in range(len(min_path)):
            st.write(f"{min_path[i] + 1} - {min_path[(i + 1) % len(min_path)] + 1} = {distance_matrix[min_path[i]][min_path[(i + 1) % len(min_path)]]}")
        
        st.write(f"Minimum cost: {min_cost}")
        st.write(f"Path Taken: {' - '.join(str(city + 1) for city in min_path)} - {min_path[0] + 1}")

except Exception as e:
    st.error(f"Error: {e}")