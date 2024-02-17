import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Books_Data_Clean.csv')

st.title('SDT Project')
st.header('Book Statistics')

st.dataframe(df)