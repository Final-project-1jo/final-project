from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from haversine import haversine
import pandas as pd
import time
import numpy as np

#벡터 구하기
def kobert(data):
    model_name = 'kykim/bert-kor-base'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    if isinstance(data, pd.Series):
        data = data.to_list()
    elif isinstance(data, str):
        data = [data]
        
    if len(data) > 1:
        all_outputs = []
        for d in data:
            tokens = tokenizer(d, return_tensors='pt', padding=True, truncation=True)
            with torch.no_grad():
                all_outputs.append(model(**tokens))
        sentences_embeddings = []
        for outputs in all_outputs:
            sentences_embeddings.append(np.array(torch.mean(outputs.last_hidden_state, dim=1).squeeze()))
        return sentences_embeddings
# target
    elif len(data) == 1:
        tokens = tokenizer(data[0], return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**tokens)
        sentence_embeddings = np.array(torch.mean(outputs.last_hidden_state, dim=1).squeeze())
        return sentence_embeddings

# 유사도 top3 찾기
def find_similarity_top_3(df, base, target):
    # base is list(np.array1, np.array2, ..., np.arrayN)
    # target is list(np.array)
    similarity_list = []
    for vec in base:
        similarity_list.append(cosine_similarity([vec], [target]))
    
    top_3_idx = []
    for sim in sorted(similarity_list, reverse=True)[:3]:
        top_3_idx.append(similarity_list.index(sim))
    return df.iloc[top_3_idx].reset_index(drop=True)

# 거리가 가까운곳 3곳 찾기
def find_near_place(base, target):
    # base is pd.DataFrame
    # target is pd.Series
    distance_list = []
    for lat, long in zip(base.Latitude, base.Longitude):
        distance_list.append(round(haversine((lat, long), (target.Latitude, target.Longitude)), 2))
    base['target_distance'] = distance_list
    base_sort_by_distance = base.sort_values(by='target_distance').reset_index(drop=True)
    return base_sort_by_distance.loc[:2]
    
    