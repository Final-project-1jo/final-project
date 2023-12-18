import sys
sys.path.append('../')
import preprocessing
from module import kobert
import pickle
import os
from googletrans import Translator


file_path = os.path.dirname(__file__)
parent_path = os.path.dirname(file_path)

embeddings = kobert(preprocessing.place_df.data)
print(embeddings)

with open(parent_path + '\\data\\kobert_embeddings.pkl', 'wb') as file:
    pickle.dump(embeddings, file)
