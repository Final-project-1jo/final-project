import streamlit as st
import pandas as pd

# 샘플 데이터프레임 생성
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E'],
        'column3' : ['a','b','c','d','e'],
         'column4' : ['1','a','3','b','5']}
df = pd.DataFrame(data)

# 현재 보여지는 행의 인덱스를 저장하는 변수
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Streamlit 애플리케이션 설정
st.title('Dataframe Viewer')

# 현재 행의 데이터프레임 표시
st.dataframe(df.iloc[st.session_state.current_index])

# 다음 행으로 이동하는 버튼
if st.button('Next Row'):
    # 현재 인덱스가 마지막 행이 아니라면 다음 행으로 이동
    if st.session_state.current_index < len(df) - 1:
        st.session_state.current_index += 1
        # 다음 행의 데이터프레임 표시
        st.write(f'{st.session_state.current_index}')
        st.dataframe(df.iloc[st.session_state.current_index])
    else:
        st.warning('마지막 행입니다.')

# 이전 행으로 이동하는 버튼 (옵션)
if st.button('Previous Row'):
    # 현재 인덱스가 첫 번째 행이 아니라면 이전 행으로 이동
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        # 이전 행의 데이터프레임 표시
        st.dataframe(df.iloc[st.session_state.current_index])
    else:
        st.warning('첫 번째 행입니다.')