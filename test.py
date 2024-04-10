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
    st.title('CSV Data Table')

    # URL of the raw CSV file on GitHub
    csv_url = 'https://github.com/ap3j/streamlit123/blob/main/salaries_cyber.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_url, nrows=100,encoding='utf-8',na_values=['NA', ''])  # Read first 100 rows

    # Display the DataFrame as a data table
    st.write(df)

if __name__ == "__main__":
    main()


