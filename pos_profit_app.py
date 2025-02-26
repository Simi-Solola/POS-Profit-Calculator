# import streamlit as st

# #Title and description of web app
# st.title("POS Business Profit Estimator")
# st.write("Calculate the profit based on the amount of cash available for withdrawals.")

# # User input: Cash available for withdrawal
# cash_available = st.number_input("Enter Cash Available for Withdrawal (₦):", min_value=1000, step=1000)

# # Key and Values for Withdrawal ranges and charges
# withdrawal_ranges = {
#     "₦1,000 - ₦5,000": (1000, 5000, 100),
#     "₦6,000 - ₦10,000": (6000, 10000, 200),
#     "₦11,000 - ₦20,000": (11000, 20000, 300),
#     "₦21,000 - ₦30,000": (21000, 30000, 400),
#     "₦31,000 - ₦40,000": (31000, 40000, 500)
# }

# # Display profit estimates
# st.write(f"### Profit Estimates for ₦{cash_available}:")
# for label, (low, high, charge) in withdrawal_ranges.items():
#     avg_withdrawal = (low + high) // 2  # Approximate average withdrawal amount
#     num_transactions = cash_available // avg_withdrawal
#     profit = num_transactions * charge
#     st.write(f"**{label}**: {num_transactions} transactions → Profit: **₦{profit}**")
    
import streamlit as st

# Title and description of web app
st.title("POS Business Profit Estimator")
st.write("Calculate the possible profit based on the amount of cash available for withdrawals.")

# User input: Cash available for withdrawal
cash_available = st.number_input("Enter Cash Available for Withdrawal (₦):", min_value=1000, step=1000)

# Key and Values for Withdrawal ranges and charges
withdrawal_ranges = {
    "₦1,000 - ₦5,000": (1000, 5000, 100),
    "₦6,000 - ₦10,000": (6000, 10000, 200),
    "₦11,000 - ₦20,000": (11000, 20000, 300),
    "₦21,000 - ₦30,000": (21000, 30000, 400),
    "₦31,000 - ₦40,000": (31000, 40000, 500),
    "₦41,000 - ₦50,000": (41000, 50000, 600)
}

# # Display profit estimates
# st.write(f"### Profit Estimates for ₦{cash_available}:")
# for label, (low, high, charge) in withdrawal_ranges.items():
#     avg_withdrawal = (low + high) // 2  # Approximate average withdrawal amount
#     num_transactions = cash_available // avg_withdrawal
#     profit = num_transactions * charge
#     st.write(f"**{label}**: {num_transactions} transactions → Profit: **₦{profit}**")

# Display profit estimates
st.write(f"### Profit Estimates for ₦{cash_available}:")
for label, (low, high, charge) in withdrawal_ranges.items():
    # Calculate avg, max and min number of transactions possible
    avg_withdrawal = (low + high) // 2  # Approximate average withdrawal amount
    max_transactions = cash_available // low  # If all transactions are at the lowest value
    min_transactions = cash_available // high  # If all transactions are at the highest value
    avg_transactions = cash_available // avg_withdrawal

    # Calculate profit based on possible scenarios
    avg_profit = avg_transactions * charge
    max_profit = max_transactions * charge
    min_profit = min_transactions * charge

    # Display results
    st.write(f"**{label}**")
    st.write(f"**Max Profit (if all withdrawals are ₦{low})**: ₦{max_profit} ({max_transactions} transactions)")
    st.write(f"**Average Profit**: {avg_transactions} transactions → Profit: **₦{avg_profit}**")
    st.write(f"**Min Profit (if all withdrawals are ₦{high})**: ₦{min_profit} ({min_transactions} transactions)")
    st.write("---")
