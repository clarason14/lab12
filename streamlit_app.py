import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('car_data.csv')

# Sidebar filters
car_name = st.sidebar.text_input('Car Name')
transmission_type = st.sidebar.multiselect('Transmission Type', options=['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

# Initialize filtered_df
filtered_df = df

# Submit button
if st.sidebar.button('Submit', key='submit1'):
    # Filter by car name if specified
    if car_name:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False)]

    # Filter by transmission type
    if transmission_type:
        filtered_df = filtered_df[filtered_df['Transmission'].isin(transmission_type)]

    # Filter by selling price range
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= selling_price_range[0]) & (filtered_df['Selling_Price'] <= selling_price_range[1])]

    # Filter by year range
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]

# Display filtered data outside the if condition to ensure it's always executed
st.write(filtered_df)
