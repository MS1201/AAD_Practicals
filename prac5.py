import streamlit as st

def min_coins(target, coins):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[target] if dp[target] != float('inf') else -1

st.title("Minimum Coins Calculator")

target = st.number_input("Enter the target amount (in Rs):", min_value=1, step=1, value=9)
coins = [1, 4, 6]

if st.button("Calculate"):
    result = min_coins(target, coins)
    if result != -1:
        st.success(f"The minimum number of coins required to make Rs. {target} is: {result}")
    else:
        st.error(f"It's not possible to make Rs. {target} with the given coin denominations.")
