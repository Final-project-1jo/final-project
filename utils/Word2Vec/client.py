import sys
sys.path.append('../')
import preprocessing
from module import tokenization, find_similarity_top_3
from gensim.models import Word2Vec
import pandas as pd
import os
import pickle

path = os.path.dirname(__file__)
parent_path = os.path.dirname(path)
# 모델 불러오기
model = Word2Vec.load(parent_path + '\\data\\word2vec_model.model')

# 사용자로부터 문장 받기
user_data = input('가고 싶은 곳에 대해 설명 해 주세요\n')

# 토큰화
user_tokens = tokenization(user_data)

# 어휘사전에 없는 단어 삭제
removed_user_tokens = []
for token in user_tokens:
    if token in model.wv:
        removed_user_tokens.append(token)

#데이터 가져오기
df = preprocessing.place_df
with open(parent_path + '\\data\\tokenized_data.pkl', 'rb') as file:
    tokenized_data = pickle.load(file)

# 유사도 가장 높은 장소 3곳
top_3_place = find_similarity_top_3(model, df, tokenized_data, removed_user_tokens)
print(top_3_place)
