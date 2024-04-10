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
# Function to render different pages based on user selection
def render_home():
    st.title("Home Page")
    st.write("This is the home page content.")
   
# Function to render About page content
def render_cybersalaries():
    st.title("About Page")
    st.write("This is the about page content.")
  
    def main():
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

if __name__ == "__main__":
    bar2()
    
# Function to render Contact page content

def render_contact():
    st.title("Contact Page")
    st.write("This is the contact page content.")
   

# Create a sidebar navigation
nav_selection = st.sidebar.radio("Navigate", ["Home", "Cyber Salaries", "Contact"])

# Render the selected page
if nav_selection == "Home":
    render_home()
elif nav_selection == "About":
    render_cybersalaries()
elif nav_selection == "Contact":
    render_contact()



