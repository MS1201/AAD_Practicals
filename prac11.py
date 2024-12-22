import streamlit as st
import numpy as np

def dijkstra(graph, start):
    n = len(graph)
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    visited = set()
    
    while len(visited) < n:
        min_node = min((node for node in range(n) if node not in visited), key=lambda node: distances[node])
        visited.add(min_node)
        
        for neighbor, weight in enumerate(graph[min_node]):
            if weight != float('inf'):
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    
    return distances


st.title("Shortest Path Finder")


num_nodes = st.number_input("Enter total number of nodes:", min_value=1, max_value=10, value=5)

start_node = st.text_input("Enter the node from where you want to calculate the distance:", value='A')

st.subheader("Enter Data (Weight):")
graph = []
for i in range(num_nodes):
    row = st.text_input(f"Row {i+1} (space-separated weights):", value=" ".join(["∞" if j != i else "0" for j in range(num_nodes)])).split()
    graph.append([float('inf') if weight == '∞' else int(weight) for weight in row])

if st.button("Calculate"):
    start_index = ord(start_node) - ord('A')
    distances = dijkstra(graph, start_index)
    
    st.subheader("Shortest Path Costs:")
    for node, cost in distances.items():
        st.write(f"Cost from {start_node} to {chr(node + ord('A'))}: {cost}")
