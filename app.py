import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Nifty_Stocks.csv')

st.title("📈 Nifty Stocks Visualization")

# Show the full DataFrame (optional)
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Dropdown for category
categories = df['Category'].unique()
selected_category = st.selectbox("Select Category", categories)

# Filter based on selected category
cat_df = df[df['Category'] == selected_category]

# Dropdown for symbol
symbols = cat_df['Symbol'].unique()
selected_symbol = st.selectbox("Select Symbol", symbols)

# Filter based on selected symbol
sym_df = cat_df[cat_df['Symbol'] == selected_symbol]

# Plotting the line chart
st.subheader(f"Closing Prices of {selected_symbol}")
fig, ax = plt.subplots(figsize=(15, 8))
sb.lineplot(data=sym_df, x='Date', y='Close', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
