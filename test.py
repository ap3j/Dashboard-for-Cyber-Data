import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to my Streamlit page!
I am a data science student at Middle Tennessee State University where I specialzie in the cyber security domain. 
I hope you get some useful insights fromy my dashboards and visualizations!

"""

def main():
    st.title('Cyber Security Salaries')

    # URL of the raw CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/ap3j/streamlit123/main/salaries_cyber.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_url, encoding='utf-8',na_values=['NA', '']) 

    # Display the DataFrame as a data table
    st.write(df)

if __name__ == "__main__":
    main()

def main():
    st.title('Salary By Experience')
    
    # Sample data
    data = {
        'Category': ['EN', 'MI', 'SN', 'EX'],
        'Value': [63579, 103337, 144560, 200706]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create Seaborn bar plot
    fig, ax = plt.subplots()
    sns.barplot(x='Category', y='Value', data=df, ax=ax)
    ax.set_title('Bar Plot')

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()


