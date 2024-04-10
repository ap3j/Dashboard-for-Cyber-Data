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
    csv_url = 'https://raw.githubusercontent.com/ap3j/streamlit123/main/salaries_cyber.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_url, nrows=100,encoding='utf-8',na_values=['NA', ''])  # Read first 100 rows

    # Display the DataFrame as a data table
    st.write(df)

if __name__ == "__main__":
    main()

sns.barplot(data=df_topsal_exp_avgsort, x='salary_in_usd', y="experience_level", 
order=df_topsal_exp_avgsort['experience_level'], color='r')
plt.title('Salary By Experience Level',fontweight='bold',fontsize='18',horizontalalignment='center')
plt.xlabel('Salary', fontweight='bold',fontsize='14',horizontalalignment='center')
plt.ylabel('Experience',fontweight='bold',fontsize='14',horizontalalignment='center')
plt.xticks(size = 5)


