import pandas as pd 
import streamlit as st 
import plotly.express as px 

df = pd.read_csv('vehicles_us.csv')

st.header('This is my fabulous header!',divider='violet')

data = df[df['price'] <= 100000]
hist_data = data['price']
histogram = px.histogram(hist_data)

st.plotly_chart(histogram)

scatter_data = df.dropna(subset='model_year')
dependent = scatter_data['price']
independent = scatter_data['model_year']
scatter_plot = px.scatter(x=independent,y=dependent)

st.plotly_chart(scatter_plot)

# st.write()
# st.checkbox()
