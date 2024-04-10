import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('car_data.csv')

# Make Filtered Data Frame
filtered_df = df

# Creating Sidebar Filters
car_name = st.sidebar.text_input('Car Name')
transmission_type = st.sidebar.multiselect('Transmission Type', options=['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

# Make Submit Button
if st.sidebar.button('Submit', key='submit1'):
    # If user inputs, filter by car name
    if car_name:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False)]
    # Filter by Transmission Type
    if transmission_type:
        filtered_df = filtered_df[filtered_df['Transmission'].isin(transmission_type)]
    # Filter by Selling Price 
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= selling_price_range[0]) & (filtered_df['Selling_Price'] <= selling_price_range[1])]
    # Filter by Year 
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]

st.write(filtered_df)