import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded", )
import pandas as pd
import numpy as np
import plotly.express as px 
from PIL import Image



import streamlit.components.v1 as components

st.sidebar.header("Real Estate Sales 2021 GL")

# Load the available data and overview

url="data/real_estate_FY2021_cleaned_project2.csv"





df = pd.read_csv(url, encoding="ISO-8859-1", low_memory=False)
    
    


menu = ['About','Sales Image','Data Analysis']
selection = st.sidebar.selectbox("Key Performance Indicator (KPI) ", menu)
st.sidebar.write('Sales Analysis refers to reviewing your sales data to identify trends and patterns. Sales data enable one or an organization to make better decisions interms of the product, pricing, promotions, inventory, customer needs and other business aspects. Sales Analysis can be as regular review of sales figures.')

if selection== 'About':
         st.header('Real Estate Sales 2021 GL')
         image=Image.open('Property.jpg')
         st.image(image,'Property Image by Paulbr75 from Pixabay')

         st.subheader("About App")
         st.markdown('The Office of Policy and Management maintains a listing of all real estate sales with a sales price of $2,000 or greater that occur between October 1 and September 30 of each year.  For each sale record, the file includes; town, property address, date of sale, property type (residential, apartment, commercial, industrial or vacant land), sales price, and property assessment.')
         st.markdown("Data are collected in accordance with Connecticut General Statutes, section 10-261a and 10-261b: https://www.cga.ct.gov/current/pub/chap_172.htm#sec_10-261a and https://www.cga.ct.gov/current/pub/chap_172.htm#sec_10-261b. Annual real estate sales are reported by grand list year (October 1 through September 30 each year). For instance, sales from 2019 GL are from 10/01/2018 through 9/30/2019.")
         st.markdown("This app provides the snapshot and brief analysis of the Real Estate Sales of 2021 GL, which is an extract from the Real Estates sales 2001 to 2021 GL dataframe. The Real Estates Sales for financial year 2021 start from 1st October 2020 all the way to 30th september 2021")

if selection== 'Sales Image' :
         st.markdown('Display data')
         st.table(df.head(3))

         st.subheader("FY-2021 Monthly Sales Performance")
         df_M= df.groupby("Sale_Month")["Sale_Amount"].sum().reset_index()
         fig=px.bar(df_M, x="Sale_Month", y="Sale_Amount", color="Sale_Month")
         st.plotly_chart(fig, theme="streamlit", use_container_width=True)

         if st.checkbox("Display Scatter Plot Establishing The Relationship Between Sale Amount And Assessed Value for FY-2021"):
           st.markdown("Click on the key to establish scatter plot of each individual Property Types")
           fig = px.scatter(df,
                 x="Assessed_Value", 
                 y="Sale_Amount", 
                 color="Property_Type",
                 hover_name="Town",
                 log_x=True,
                 log_y=True,
                 )
           st.plotly_chart(fig, theme="streamlit", use_container_width=True)

         if st.checkbox('Display Sales By Property And Residential Type for FY-2021'):
           col1, col2 = st.columns(2)

           with col1:
                st.subheader("FY-2021 Sales by Property Type")
                data_Ptype=df.groupby(['Property_Type']).size().reset_index(name="Count")
                data_Ptype['Count%']=(data_Ptype['Count']/sum(data_Ptype['Count']))*100
                fig=px.bar(data_Ptype, x="Property_Type", y="Count", color="Property_Type")
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)

           with col2:
                st.subheader("FY-2021 Sales by Residential Type")
                data_Rtype=df.groupby(['Residential_Type']).size().reset_index(name='Count')
                data_Rtype["Counts%"]=(data_Rtype['Count']/sum(data_Rtype['Count']))*100
                fig=px.pie(data_Rtype, values="Counts%", names = 'Residential_Type', title= "Sales By Residential Type", hover_data=['Count'])
                fig.update_traces(textposition='inside',textinfo='percent+label')
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)


if selection== 'Data Analysis':
         st.markdown('Display data')
         st.write(df.head())

    # shape of data
         if st.checkbox("show shape "):
          st.write('Data Shape')
          st.write('{:,} rows; {:,} columns'.format(df.shape[0], df.shape[1]))

        # data description
          st.markdown("Descriptive statistics for FY-2021")
          st.write(df[['Assessed_Value','Sale_Amount']].describe())

         if st.checkbox("Show Frequency Tables For Property And Residential Type for FY-2021"):
           col1, col2 = st.columns(2)

           with col1:
                st.subheader("Frequency Table for Property Type for FY-2021")
                data_Ptype=df.groupby(['Property_Type']).size().reset_index(name="Count")
                data_Ptype["Counts%"]=(data_Ptype['Count']/sum(data_Ptype['Count']))*100
                st.write(data_Ptype)

           with col2:
                st.subheader("Frequency Table For Residential Type for FY-2021")
                data_Rtype=df.groupby(['Residential_Type']).size().reset_index(name='Count')
                data_Rtype["Counts%"]=(data_Rtype['Count']/sum(data_Rtype['Count']))*100
                st.write(data_Rtype)
 