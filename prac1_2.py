import streamlit as st
import itertools

def find_closest_to_zero(numbers):
    if len(numbers) < 2:
        return None
    
    combinations = list(itertools.combinations(numbers, 2))
    closest_sum = float('inf')
    closest_pairs = []

    for pair in combinations:
        current_sum = abs(sum(pair))
        if current_sum < closest_sum:
            closest_sum = current_sum
            closest_pairs = [pair]
        elif current_sum == closest_sum:
            closest_pairs.append(pair)

    return closest_pairs

st.title("Find Pairs Closest to Zero")

numbers_input = st.text_input("Enter numbers separated by commas:", "15, 5, -20, 30, -45")

if st.button("Find Closest Pairs"):
    numbers = [int(num.strip()) for num in numbers_input.split(',')]
    
    result = find_closest_to_zero(numbers)

    st.write(f"Input numbers: {numbers}")
    
    if result:
        st.write("Closest pair(s):")
        for pair in result:
            st.write(f"{pair[0]}, {pair[1]} (Sum: {sum(pair)})")
    else:
        st.write("Not enough numbers to form a pair.")