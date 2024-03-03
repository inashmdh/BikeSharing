import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

# Set the option to suppress the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the provided DataFrame
day_df = pd.read_csv("Dashboard/all_data.csv")
# Add a sidebar with image
st.sidebar.title("Inas Hamidah")
st.sidebar.header("Projek Akhir Dicoding")
st.sidebar.image("sepeda.jpg", caption="Bike Sharing Analyst", use_column_width=True)

# Add a calendar to the sidebar
selected_date = st.sidebar.date_input("Select Date", date.today())


# Pertanyaan 1: Bike Rentals by Season
st.subheader('🚲Bike Rentals by Season🚲')

# Split the layout into two columns
col1, col2 = st.columns(2)

# Bar plot in the first column
with col1:
    # Set the size of the plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Define a custom color palette
    custom_palette = ["pink", "green", "purple", "beige"]

    # Create a bar plot using seaborn with the custom color palette
    sns.barplot(
        y="cnt",
        x="season",
        data=day_df.sort_values(by="season", ascending=False),
        palette=custom_palette,
        ax=ax  # Pass the axis explicitly
    )

    # Add title and adjust layout
    plt.title("Bike Rentals by Season", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis="x", labelsize=12)

    # Display the plot using Streamlit
    st.pyplot(fig)

# Metrics in the second column
with col2:
    total_rentals = day_df["cnt"].sum()
    st.metric("Total Rentals", value=total_rentals)

# Pertanyaan 2: Temperature vs Bike Rentals
st.subheader('Temperature vs Bike Rentals')

# Split the layout into two columns
col1, col2 = st.columns(2)

# Scatter plot in the first column
with col1:
    # Create a scatter plot with matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df)
    plt.title('Scatter Plot: Temperature vs Bike Rentals')
    st.pyplot(fig)

# Heatmap in the second column
with col2:
    # Create a heatmap with seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(day_df[['temp', 'cnt']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap: Temperature vs Bike Rentals')
    st.pyplot(fig)

# Pertanyaan 3: Weather Situation vs Bike Rentals
st.subheader('Weather Situation vs Bike Rentals')

# Split the layout into two columns
col1, col2 = st.columns(2)

# Box plot in the first column
with col1:
    # Set the size of the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Define a custom color palette
    custom_palette = ["yellow", "green", "beige"]

    # Create a box plot using seaborn with the custom color palette
    sns.boxplot(x='weathersit', y='cnt', data=day_df, palette=custom_palette, ax=ax)

    # Add title
    plt.title('Boxplot: Correlation between Weather and Bike Rentals')
    st.pyplot(fig)

# Metrics in the second column
with col2:
    total_rentals = day_df["cnt"].sum()
    st.metric("Total Rentals", value=total_rentals)
