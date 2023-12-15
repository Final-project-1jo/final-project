import streamlit as st
from utils.KoBERT import client
import pickle



def desc():
    user_input_data = st.text_input('Please describe where you would like to travel.')
    top_3_df, near_hotels = client.app(user_input_data)
    st.write(f'첫번째 추천 : {top_3_df.name[0]}')
    st.info(f"{top_3_df['info'][0]}")
