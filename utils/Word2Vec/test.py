from googletrans import LANGUAGES
import os
from googletrans import Translator
import client

hotel, food =client.app1(client.place_df.iloc[3])
print(hotel)
print(food)