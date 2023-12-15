import sys
sys.path.append('../')
import preprocessing
from module import tokenization
import pickle
import os

file_path = os.path.dirname(__file__)
parent_path = os.path.dirname(file_path)

df = preprocessing.place_df
tokenized_data = tokenization(df.data)
with open(parent_path + '\\data\\tokenized_data.pkl', 'wb') as file:
    pickle.dump(tokenized_data, file)

