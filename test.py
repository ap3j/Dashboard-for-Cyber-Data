import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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

def bar():
    st.title('Salary By Experience')
    
    # Sample data
    data = {
        'Category': ['EN', 'MI', 'SN', 'EX'],
        'Value': [63579, 103337, 144560, 200706]
    }

    # Create DataFrame
    df_topsal = pd.DataFrame(data)

    # Create Seaborn bar plot
    fig, ax = plt.subplots()
    sns.barplot(x='Category', y='Value', data=df_topsal, ax=ax)
    ax.set_title('Bar Plot')

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    bar()

def bar2():
    st.title('Salary By Job Title Top 5')
    
    # Sample data
    data = {
        'Value': [315000, 295000, 260000, 237000,235540],
        'Job Title': 'Category': ['Application Security Architect', 'Staff Security Engineer', 'Threat Intellgience Response Analyst', 
                     'Principal Applicaiton Security Engineer','Software Security Engineer']
    }

    # Create DataFrame
    df_topsal5 = pd.DataFrame(data)

    # Create Seaborn bar plot
    fig, ax = plt.subplots()
    sns.barplot(x='Category', y='Value', data=df_topsal, ax=ax)
    ax.set_title('Bar Plot')

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    bar2()
