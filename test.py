import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to my Streamlit page!
I am a data science student at Middle Tennessee State University where I specialzie in the cyber security domain. 
I hope you get some useful insights fromy my dashboards and visualizations!

"""
csv_url = 'https://github.com/ap3j/streamlit123/blob/main/salaries_cyber.csv'

data = pd.read_csv_(csv_url)
