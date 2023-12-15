from konlpy.tag import Okt
import pandas as pd
import os
import pickle

path = os.path.dirname(__file__)
parent_path = os.path.dirname(path)

#불용어
def call_stopwords():
    with open(parent_path + '\\data\\stopwords.txt', 'r', encoding='utf-8') as file:
        word_list=[]
        lines = file.readlines()
        for line in lines:
            word_list.extend(line.replace("'", '').replace(' ', '').split(','))
    word_list = list(set(word_list))
    word_list.remove('')
    return word_list

# 토큰화
def tokenization(data):
    stopwords = call_stopwords()
    okt = Okt()
    if isinstance(data, pd.Series):
        data = data.str.replace(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', regex=True)
        tokenized_data = []
        for sentence in data:
            tokens = okt.morphs(sentence, stem=True)
            stopwords_remove_tokens = [token for token in tokens if not token in stopwords]
            tokenized_data.append(stopwords_remove_tokens)
    elif isinstance(data, str):
        data = pd.Series(data).str.replace(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', regex=True)[0]
        tokens = okt.morphs(data, stem=True)
        tokenized_data = [token for token in tokens if not token in stopwords]

    return tokenized_data

# 유사도 가장 높은 장소 3곳
def find_similarity_top_3(model, df, base, target):
    sim_list = []
    for data in base:
        sim_list.append(model.wv.n_similarity(data, target))
    df['target_similarity'] = sim_list
    return df.sort_values(by='target_similarity', ascending=False, ignore_index=True).iloc[:3].name