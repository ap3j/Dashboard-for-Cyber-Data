import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to my Streamlit page!


"""
# Function to render different pages based on user selection

def main1():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Cyber Salaries", "Contact Page"])

    if page == "Home Page":
        render_home()
    elif page == "Cyber Salaries":
        render_cybersalaries()
    elif page == "Contact Page":
        render_contact()
        
def render_home():
    st.title("Home Page")
    st.write("I am a data science student at Middle Tennessee State University where I specialzie in the cyber security domain. I hope you get some useful insights fromy my dashboards and visualizations")
   
# Function to render About page content
def render_cybersalaries():
    st.title("Cyber Salaries")
    st.write("Salary Graphs and Visualizations Below")
  
def main2():
    st.title('Cyber Salaries')
    
    # URL of the raw CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/ap3j/streamlit123/main/salaries_cyber.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_url, encoding='utf-8',na_values=['NA', '']) 

        # Display the DataFrame as a data table
    st.write(df)
    
    if __name__ == "__main__":
        main2()

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


def bar2():
    st.title('Salary By Job Title Top 5')
    
    # Sample data
    data = {
        'Value': [315000, 295000, 260000, 237000,235540],
        'Job Title': ['Application Security Architect', 'Staff Security Engineer', 'Threat Intellgience Response Analyst', 
                     'Principal Applicaiton Security Engineer','Software Security Engineer']
    }

    # Create DataFrame
    df_topsal15 = pd.DataFrame(data)

    # Create Seaborn bar plot
    fig, ax = plt.subplots()
    sns.barplot(x='Value', y='Job Title', data=df_topsal15, ax=ax)
    ax.set_title('Bar Plot')

    # Display the plot in Streamlit
    st.pyplot(fig)


    
# Function to render Contact page content

def render_contact():
    st.title("Contact Page")
    st.write("Contact me at ap3j@mtmail.mtsu.edu")

if __name__ == "__main__":
    main1()
   





