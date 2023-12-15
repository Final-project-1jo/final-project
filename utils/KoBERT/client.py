from module import find_similarity_top_3, kobert, find_near_place
import pandas as pd
import os
import pickle

# 유사도 top 3
file_path = os.path.dirname(__file__)
parent_path = os.path.dirname(file_path)
place_df = pd.read_csv(parent_path + '\\data\\place.csv')

with open(parent_path + '\\data\\kobert_embeddings.pkl', 'rb') as file:
    base_embeddings = pickle.load(file)

# 정보받기
user_data = input('가고 싶은 곳에 대해 설명 해 주세요\n')
target_embedding = kobert(user_data)


top_3_df = find_similarity_top_3(place_df, base_embeddings, target_embedding)

#유사도가 가장 높은 장소와 가장 가까운 숙소 3곳
hotel_df = pd.read_csv(parent_path + '\\data\\hotel.csv')

near_hotels = find_near_place(hotel_df, top_3_df.loc[0])

# 장소 , 링크 데이터 불러오기
with open(parent_path + '\\data\\name_link_dict.pkl', 'rb') as file:
    name_link_dict = pickle.load(file)

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