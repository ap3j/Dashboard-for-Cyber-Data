import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to my Streamlit Cyber Security Dataset page!


"""
# Function to render different pages based on user selection

def main1():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Cyber Salaries", "Data Breaches","Malware", "Contact Page"])

    if page == "Home":
        render_home()
    elif page == "Cyber Salaries":
        render_cybersalaries()
    elif page == "Data Breaches":
        render_databreach()
    elif page == "Malware":
        render_malware()
    elif page == "Contact Page":
        render_contact()
        
def render_home():
    st.title("Home Page")
    st.write("I am a data science student at Middle Tennessee State University where I specialize in cyber security as my data domain. On average, a cyber attack occurs every 39 seeconds affecting 1 out of three Americans. The average cost of a databreach is 3 to 4 million USD. Cyber security is a wrothwhile investment for any organization.")
    st.write("My streamlit page looks at salaries of cyber security professionals, databreaches, and network attacks. I hope you find my analysis and inights useful!")
    st.write("Credits to these three Kaggle sources for providing the datasets!")
 # Create a hyperlink
    st.markdown('[Cyber Salaries from Deep Contractor](https://www.kaggle.com/datasets/deepcontractor/cyber-security-salaries)')
    st.markdown('[Data Breaches from The Devastator](https://www.kaggle.com/datasets/thedevastator/data-breaches-a-comprehensive-list)')
    st.markdown('[Malware Detection from Agung Pambudi](https://www.kaggle.com/datasets/agungpambudi/network-malware-detection-connection-analysis)')
   
# Function to render About page content

def render_cybersalaries():
    st.title("Cyber Salaries")
    st.write("Cyber security salaries are important to understand market trends and movement for when hiring cyber security staff. Visualization and graphs below.")
  
    def main2():
        st.title('Dataset')
    
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


def render_databreach():
    st.title("Data Breach")
    st.write("Databreaches are significant because attackers can retrieve and encrpyt sensitive data. Graphs and Visualizations are shown below.")

    def main3():
        st.title('Dataset')
    
    # URL of the raw CSV file on GitHub
        csv_url = 'https://raw.githubusercontent.com/ap3j/streamlit123/main/df_1.csv'

    # Read the CSV file into a DataFrame
        df= pd.read_csv(csv_url, encoding='utf-8',na_values=['NA', '']) 

        # Display the DataFrame as a data table
        st.write(df)
    
    if __name__ == "__main__":
     main3()

    def bar4():
        st.title('Top 5 Industries for Databreaches')
    
    # Sample data
        data = {'Value': [53, 47, 38, 30,27],'Job Title': ['Web', 'Healthcare', 'Financial', 'Government','Retail']}

    # Create DataFrame
        df_breach = pd.DataFrame(data)

    # Create Seaborn bar plot
        fig, ax = plt.subplots()
        sns.barplot(x='Value', y='Job Title', data=df_breach, ax=ax)
        ax.set_title('Bar Plot')

    # Display the plot in Streamlit
        st.pyplot(fig)

    if __name__ == "__main__":
        bar4()

    def bar5():
        st.title('Top Methods Used By Attackers')
    
    # Sample data
        data = {
            'Category': ['Hacked', 'Poor Security', 'Stolen Media', 'Accidental Publish'],
            'Value': [192, 43, 33, 21]
        }

        # Create DataFrame
        df_topmeth = pd.DataFrame(data)

    # Create Seaborn bar plot
        fig, ax = plt.subplots()
        sns.barplot(x='Category', y='Value', data=df_topmeth, ax=ax)
        ax.set_title('Bar Plot')

    # Display the plot in Streamlit
        st.pyplot(fig)
   
    if __name__ == "__main__":
     bar5()

    
# Function to render Contact page content

def render_malware():
    st.title("Malware")
    st.write("Malware and malware traffic are important to understand as a cybersecurity professional. Visualization and graphs below.")

    def main4():
        st.title('Dataset')
    
    # URL of the raw CSV file on GitHub
        csv_url = 'https://raw.githubusercontent.com/ap3j/streamlit123/main/CTU-IoT-Malware-Capture-3-1conn.log.labeled.csv'

    # Read the CSV file into a DataFrame
        df= pd.read_csv(csv_url, encoding='utf-8',na_values=['NA', ''], sep='|') 

        # Display the DataFrame as a data table
        st.write(df)
    
    if __name__ == "__main__":
     main4()

    def bar6():
        st.title('Top 5 Malicious IP Addresses')
    
    # Sample data
        data = {
            'Value': [23295, 77, 76, 76,76],
            'IP Addresses': ['200.168.87.203', '148.251.4.51', '182.253.179.62', 
                     '203.242.197.223','144.76.156.49']
        }

    # Create DataFrame
        df_topip = pd.DataFrame(data)

    # Create Seaborn bar plot
        fig, ax = plt.subplots()
        sns.barplot(x='Value', y='IP Addresses', data=df_topip, ax=ax)
        ax.set_title('Bar Plot')

    # Display the plot in Streamlit
        st.pyplot(fig)

    if __name__ == "__main__":
     bar6()

    def bar7():
        st.title('Top three ports for attacks')
    
    # Sample data
        data = {'Ports': ['22', '59353', '2407'],'Value': [128264, 23295, 8]}

        # Create DataFrame
        df_topports = pd.DataFrame(data)

    # Create Seaborn bar plot
        fig, ax = plt.subplots()
        sns.barplot(x='Ports', y='Value', data=df_topports, ax=ax)
        ax.set_title('Bar Plot')

    # Display the plot in Streamlit
        st.pyplot(fig)
   
    if __name__ == "__main__":
     bar7()




def render_contact():
    st.title("Contact Page")
    st.write("Contact me at ap3j@mtmail.mtsu.edu")

if __name__ == "__main__":
    main1()
   





