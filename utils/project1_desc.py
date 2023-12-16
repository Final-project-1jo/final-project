import streamlit as st
from utils.KoBERT import client
import pickle
import os

def desc():
    user_input_data = st.text_input('Please describe where you would like to travel.')
    top_3_df, near_hotels, near_foods = client.app(user_input_data)
    top_3_df_first = f"<a href='{top_3_df.link[0]}'>{top_3_df.name[0]}</a>"
    st.markdown(top_3_df_first, unsafe_allow_html=True)
    st.info(f"{top_3_df['info'][0]}")
    col0, col1 = st.columns(2)
    with col0:
        st.write('Nearby foods')
        st.markdown(f"<a href='{near_foods.link[0]}'>{near_foods.name[0]}</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{near_foods.link[1]}'>{near_foods.name[1]}</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{near_foods.link[2]}'>{near_foods.name[2]}</a>", unsafe_allow_html=True)
    with col1:
        st.write('Nearby hotels')
        st.markdown(f"<a href='{near_hotels.link[0]}'>{near_hotels.name[0]}</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{near_hotels.link[1]}'>{near_hotels.name[1]}</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{near_hotels.link[2]}'>{near_hotels.name[2]}</a>", unsafe_allow_html=True)

