from pyparsing import col
import streamlit as st
from plotly import express as px
import plotly.graph_objects as go

import pandas as pd
from textblob import TextBlob
import numpy as np
import os
import re

#import data

df = pd.read_csv(r'C:\Users\andre\Desktop\Experiments\model-creation\cook-book-reviews\Cookbook Reviews.csv')
df.drop(columns=['rec_cd', 'rec_no', 'cmt_id', 'user_id'], inplace=True)
df = df.rename(columns={'rec_nm':'recipe_name', 'user_nm': 'user_name', 
                   'user_reput': 'user_behavior', 'response_no': 'comment_response'})
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
df['date'] = pd.to_datetime(df['datetime'].values)
# df['date'] = df['date'].to_timestamp()
df.drop(columns=['timestamp'], inplace=True)
df = df[df['ratings']!=0].reset_index(drop=True)


def text_polarity(text):
    return TextBlob(text).sentiment.polarity


def text_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def text_sentiment(score):
    if score<0:
        return 'negative'
    elif score==0: 
        return 'neutral'
    else:
        return 'positive'


df['comment'] = df['comment'].astype(str)
df['polarity'] = df['comment'].apply(text_polarity)
df['subjectivity'] = df['comment'].apply(text_subjectivity)
df['sentiment'] = df['polarity'].apply(text_sentiment)


# st.set_pages_con
st.set_page_config(page_title="Cook-Book",layout='wide')

st.header(':cooking: Recipe Text Analysis')
tab1, tab2 = st.tabs(['Exploration', 'Predictions'])

with st.sidebar:
    
    dates =  df['date'].dt.year.unique().tolist()
    st.markdown('Select year')

    st.checkbox(f'{min(dates)}',value=True)
    st.checkbox(f'{max(dates)}', value=True)
    st.multiselect('Rating', df['ratings'].unique())````````````````

    st.multiselect('Recipe',df['recipe_name'].unique())
    
    

with tab1:
    col1, col2= st.columns([0.6,0.4])
    with col1: 
        date_by_rating = df.groupby(['datetime', 'sentiment'])['ratings'].agg('mean').reset_index()
        date_by_rating['year'] = df.datetime.dt.year
        date_by_rating['month'] = df.datetime.dt.month_name()
        data_2021 = date_by_rating[date_by_rating.year==2022]
        f1 = data_2021.groupby('month', as_index=False)['ratings'].mean().sort_values('month', ascending=False)

        fig= px.line(f1, x='month', y='ratings', height=300,)
        st.plotly_chart(fig, use_container_width=True)
        # px.imshow()
    with col2:
        ratings_prop = df.ratings.value_counts(normalize=True).to_frame().reset_index()
        fig = px.pie(data_frame=ratings_prop,values='proportion',
                    names='ratings', hole=0.4, height=300
                    )
        fig.update_layout(title='Ratings distribution')
        fig.update_legends(title='Ratings')
        st.plotly_chart(fig, use_container_width=True)
    
    

        
        
    