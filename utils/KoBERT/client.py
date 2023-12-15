from utils.KoBERT.module import find_similarity_top_3, kobert, find_near_place
from googletrans import Translator # pip install googletrans==4.0.0-rc1
import pandas as pd
import os
import pickle


file_path = os.path.dirname(__file__)
parent_path = os.path.dirname(file_path)

#여행지 데이터 불러오기
place_df = pd.read_csv(parent_path + '\\data\\place.csv')

#숙소 데이터 불러오기
hotel_df = pd.read_csv(parent_path + '\\data\\hotel.csv')

#임베딩된 문장들 불러오기
with open(parent_path + '\\data\\kobert_embeddings.pkl', 'rb') as file:
    base_embeddings = pickle.load(file)

# 장소 , 링크 데이터 불러오기
with open(parent_path + '\\data\\name_link_dict.pkl', 'rb') as file:
    name_link_dict = pickle.load(file)

def app(user_text):
    translator = Translator()
    # 언어 감지 후 번역
    trans_user_text_data = translator.translate(user_text, dest='ko')
    trans_user_text = trans_user_text_data.text
    trans_from_lang = trans_user_text_data.src
    trans_to_lang = trans_user_text_data.dest # maybe, KOREAN
    
    target_embedding = kobert(trans_user_text)

    #유사도 높은 장소 3곳
    top_3_df = find_similarity_top_3(place_df, base_embeddings, target_embedding)

    #유사도가 가장 높은 장소와 가장 가까운 숙소 3곳
    near_hotels = find_near_place(hotel_df, top_3_df.loc[0])

    # 대상언어로 번역
    for idx, name in enumerate(top_3_df.name):
        top_3_df.name[idx] = translator.translate(name, src=trans_to_lang, dest=trans_from_lang).text
    for idx, info in enumerate(top_3_df['info']):
        top_3_df['info'][idx] = translator.translate(info, src=trans_to_lang, dest=trans_from_lang).text
    for idx, name in enumerate(near_hotels.name):
        near_hotels.name[idx] = translator.translate(name, src=trans_to_lang, dest=trans_from_lang).text
    for idx, info in enumerate(near_hotels['info']):
        near_hotels['info'][idx] = translator.translate(info, src=trans_to_lang, dest=trans_from_lang).text
    #유사도가 가장 높은 장소와 가장 가까운 음식점 3곳
    #near_foods = 
    return top_3_df, near_hotels

'''
print(f'추천 여행지 \n{top_3_df.name[0]}')
print(name_link_dict[top_3_df.name[0]])
print(f'이곳도 가보는건 어때요?\n {top_3_df.name[1]} \n {top_3_df.name[2]}')

print('여행지와 가까운 숙소')
print(f'{near_hotels.name[0]}')
print(f'{name_link_dict[near_hotels.name[0]]}')
print(f'{near_hotels.name[1]}')
print(f'{name_link_dict[near_hotels.name[1]]}')
print(f'{near_hotels.name[2]}')
print(f'{name_link_dict[near_hotels.name[2]]}')
'''