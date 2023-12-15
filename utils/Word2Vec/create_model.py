import sys
sys.path.append('../')
import preprocessing
from gensim.models import Word2Vec
from module import tokenization
import os

file_path = os.path.dirname(__file__)
parent_path = os.path.dirname(file_path)
#데이터 불러오기
df = preprocessing.place_df

# 토큰화
tokenized_data = tokenization(df.data)

# 모델 생성 및 저장
## 오류시 pip install --upgrade gensim
model = Word2Vec(tokenized_data, vector_size=100, window=5, min_count=5, workers=4, epochs=35)
model.save(parent_path + '\\data\\word2vec_model.model')


