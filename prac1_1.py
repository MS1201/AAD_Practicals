import streamlit as st

st.title("MasterChef Competition Comparison")

def compare_chefs(a, b):
    chef1_points = 0
    chef2_points = 0
    for i in range(3):
        if a[i] > b[i]:
            chef1_points += 1
        elif a[i] < b[i]:
            chef2_points += 1
    return [chef1_points, chef2_points]

st.write("Enter ratings for each chef (Presentation, Taste, Hygiene):")

chef1_ratings = []
for category in ["Presentation", "Taste", "Hygiene"]:
    rating = st.number_input(f"Chef 1 - {category}", min_value=1, max_value=100, value=50, key=f"chef1_{category}")
    chef1_ratings.append(rating)

chef2_ratings = []
for category in ["Presentation", "Taste", "Hygiene"]:
    rating = st.number_input(f"Chef 2 - {category}", min_value=1, max_value=100, value=50, key=f"chef2_{category}")
    chef2_ratings.append(rating)

if st.button("Compare Chefs"):
    result = compare_chefs(chef1_ratings, chef2_ratings)
    st.write(f"Comparison points: Chef 1: {result[0]}, Chef 2: {result[1]}")
    
    st.write("Explanation:")
    categories = ["Presentation", "Taste", "Hygiene"]
    for i in range(3):
        if chef1_ratings[i] > chef2_ratings[i]:
            st.write(f"{categories[i]}: Chef 1 wins ({chef1_ratings[i]} > {chef2_ratings[i]})")
        elif chef1_ratings[i] < chef2_ratings[i]:
            st.write(f"{categories[i]}: Chef 2 wins ({chef1_ratings[i]} < {chef2_ratings[i]})")
        else:
            st.write(f"{categories[i]}: Tie ({chef1_ratings[i]} = {chef2_ratings[i]})")

   
