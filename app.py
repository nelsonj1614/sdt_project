# Import libraries
import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px

# Load file and clean
df = pd.read_csv('Books_Data_Clean.csv')
df.drop(columns=['index','language_code','Author_Rating','sales rank'],inplace=True)
df.columns = ['publishing_year','book_name','author','book_average_rating',
              'book_ratings_count','genre','gross_sales','publisher_revenue','sales_price',
              'publisher','units_sold']
df['genre'].replace('genre fiction','fiction',inplace=True)
df['publisher'].replace('Amazon Digital Services,  Inc.','Amazon Digital Services, Inc.',inplace=True)
df['book_name'].fillna('Unknown',inplace=True)

# Design app
st.header('Book Sales')

check = st.checkbox('Only fiction')
check_2 = st.checkbox('Only nonfiction')
check_3 = st.checkbox('Only books for children')

df_fiction = df[df['genre'] == 'fiction']
df_nonfiction = df[df['genre'] == 'nonfiction']
df_children = df[df['genre'] == 'children']

if check:
    st.write(df_fiction)
elif check_2:
    st.write(df_nonfiction)
elif check_3:
    st.write(df_children)
else:
    st.dataframe(df)

st.divider()

# Books by year by publisher
recent = df[df['publishing_year'] >= 2000]
by_year = recent.groupby(['publishing_year','publisher'])['book_name'].count().reset_index()
by_year.columns = ['publishing_year','publisher','count']
chart_2 = px.bar(by_year,x='publishing_year',y='count',color='publisher',title='Number of Books Published Per Year')
st.plotly_chart(chart_2)

st.divider()

# Revenue by Year by Publisher

rev_by_pub = recent.groupby(['publishing_year','publisher'])['publisher_revenue'].sum().reset_index()
chart_3 = px.line(rev_by_pub,x='publishing_year',y='publisher_revenue',color='publisher',title='Revenue by Year by Publisher')
st.plotly_chart(chart_3)

# Units sold Distribution by Publisher
st.header('Gross Sales by Book by Publisher')

gross_sales = df['gross_sales']
total_sales = px.histogram(gross_sales,x='gross_sales',nbins=100,title='Distribution of gross sales by book')

selectbox = st.selectbox('Select an option',('All','Amazon','HarperCollins','Penguin','Random House','Hachette'))

only_am = df[df['publisher'] == 'Amazon Digital Services, Inc.']
am_sold = only_am['gross_sales']
total_am_sold = px.histogram(am_sold,x='gross_sales',nbins=100,title='Distribution of gross sales by Amazon')

only_harp = df[df['publisher'] == 'HarperCollins Publishers']
harp_sold = only_harp['gross_sales']
total_harp_sold = px.histogram(harp_sold,x='gross_sales',nbins=100,title='Distribution of gross sales by Harper Collins')

only_Pen = df[df['publisher'] == 'Penguin Group (USA) LLC']
Pen_sold = only_Pen['gross_sales']
total_pen_sold = px.histogram(Pen_sold,x='gross_sales',nbins=100,title='Distribution of gross sales by Penguin Group')

only_Ran = df[df['publisher'] == 'Random House LLC']
Ran_sold = only_Ran['gross_sales']
total_ran_sold = px.histogram(Ran_sold,x='gross_sales',nbins=100,title='Distribution of gross sales by Random House')

only_Ha = df[df['publisher'] == 'Hachette Book Group']
Ha_sold = only_Ha['gross_sales']
total_ha_sold = px.histogram(Ha_sold,x='gross_sales',nbins=100,title='Distribution of gross sales by Hachette Book Group')

if selectbox == 'HarperCollins':
    st.plotly_chart(total_harp_sold)
elif selectbox == 'Penguin':
    st.plotly_chart(total_pen_sold)
elif selectbox == 'Random House':
    st.plotly_chart(total_ran_sold)
elif selectbox == 'Hachette':
    st.plotly_chart(total_ha_sold)
elif selectbox == 'Amazon':
    st.plotly_chart(total_am_sold)
else:
    st.plotly_chart(total_sales)

st.write('You are displaying', selectbox)

st.divider()

# Scatter plot showing relationship between book rating and gross sales
st.header('Relationship between book rating and gross sales')

books_2010 = df[df['publishing_year'] == 2010]
scat_2010 = px.scatter(books_2010,x='book_average_rating',y='gross_sales')
books_2011 = df[df['publishing_year'] == 2011]
scat_2011 = px.scatter(books_2011,x='book_average_rating',y='gross_sales')
books_2012 = df[df['publishing_year'] == 2012]
scat_2012 = px.scatter(books_2012,x='book_average_rating',y='gross_sales')
books_2013 = df[df['publishing_year'] == 2013]
scat_2013 = px.scatter(books_2013,x='book_average_rating',y='gross_sales')
books_2014 = df[df['publishing_year'] == 2014]
scat_2014 = px.scatter(books_2014,x='book_average_rating',y='gross_sales')
books_2015 = df[df['publishing_year'] == 2015]
scat_2015 = px.scatter(books_2015,x='book_average_rating',y='gross_sales')
books_2016 = df[df['publishing_year'] == 2016]
scat_2016 = px.scatter(books_2016,x='book_average_rating',y='gross_sales')

slider = st.slider('Select a Year Between 2010 and 2016',min_value=2010,max_value=2016,step=1)

if slider == 2010:
    st.plotly_chart(scat_2010)
elif slider == 2011:
    st.plotly_chart(scat_2011)
elif slider == 2012:
    st.plotly_chart(scat_2012)
elif slider == 2013:
    st.plotly_chart(scat_2013)
elif slider == 2014:
    st.plotly_chart(scat_2014)
elif slider == 2015:
    st.plotly_chart(scat_2015)
else:
    st.plotly_chart(scat_2016)

st.write('Year', slider)

st.divider()