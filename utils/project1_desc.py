import streamlit as st
from utils.Word2Vec import client, module
import os
from googletrans import LANGUAGES, Translator

def desc():
    st.write('Select just one tag at first, and if you don't find what you want, select more.')
    languages = {name:code for code, name in LANGUAGES.items()}
    s_box = st.selectbox('choice languages', tuple(languages.keys()))
    korean_to_target_list, target_to_korean_dict = module.show_tag(languages[s_box])
    col0, col1, col2 = st.columns(3)
    with col0:
        s_box0 = st.selectbox('choice tag', tuple(korean_to_target_list))
    with col1:
        s_box1 = st.selectbox('choice tag', ('X', ) + tuple(korean_to_target_list), key='s_box1_key')
    with col2:
        s_box2 = st.selectbox('choice tag', ('X', ) + tuple(korean_to_target_list), key='s_box2_key')
    s_boxes= [s_box0, s_box1, s_box2]
    user_data = [target_to_korean_dict[tag] for tag in s_boxes if not 'X' in tag]
    place_df = client.app0(user_data)
    
    if 'current_index' not in st.session_state or st.session_state.s_box != s_box or any(st.session_state.s_boxes[i] != s_boxes[i] for i in range(len(s_boxes))):
        st.session_state.current_index = 0

    st.session_state.s_box = s_box
    st.session_state.s_boxes = s_boxes

    if st.button('Show Place'):
        if st.session_state.current_index < len(place_df) + 1:
            st.session_state.current_index += 1
            st.write(f'Place Rank ,{st.session_state.current_index}')
            best_similarity_place = f"<a href='{place_df.link[st.session_state.current_index - 1]}'>{Translator().translate(place_df.name[st.session_state.current_index - 1], src='ko', dest=languages[s_box]).text}</a>"
            st.markdown(best_similarity_place, unsafe_allow_html=True)

            near_hotel_df, near_food_df = client.app1(place_df.iloc[st.session_state.current_index - 1])
            col0, col1 = st.columns(2)
            with col0:
                st.write('Nearby foods')
                st.markdown(f"<a href='{near_food_df.link[0]}'>{near_food_df.name[0]}</a>", unsafe_allow_html=True)
                st.markdown(f"<a href='{near_food_df.link[1]}'>{near_food_df.name[1]}</a>", unsafe_allow_html=True)
                st.markdown(f"<a href='{near_food_df.link[2]}'>{near_food_df.name[2]}</a>", unsafe_allow_html=True)
            with col1:
                st.write('Nearby hotels')
                st.markdown(f"<a href='{near_hotel_df.link[0]}'>{near_hotel_df.name[0]}</a>", unsafe_allow_html=True)
                st.markdown(f"<a href='{near_hotel_df.link[1]}'>{near_hotel_df.name[1]}</a>", unsafe_allow_html=True)
                st.markdown(f"<a href='{near_hotel_df.link[2]}'>{near_hotel_df.name[2]}</a>", unsafe_allow_html=True)

