import os
import sys
import urllib.request
import json

id = '5VzlTHx3tgwK2VbWr296'
secret = 'rvu4XGsqAj'
trans_possible_lang_list = ['ko', 'en', 'ja', 'zh-CN', 'zh-TW', 'vi', 'id', 'th', 'de', 'ru', 'es', 'it', 'fr']

def detectLangs(text):
    encQuery = urllib.parse.quote(text)
    data = 'query=' + text
    url = 'https://openapi.naver.com/v1/papago/detectLangs'
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', id)
    request.add_header('X-Naver-Client-Secret', secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        #return response_body.decode('utf-8')
        return json.loads(response_body)
    else:
        print('error!')

def translate(text, source, target):
    encText = urllib.parse.quote(text)
    data = 'source=' + source + '&target=' + target + '&text=' + encText
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', id)
    request.add_header('X-Naver-Client-Secret', secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return json.loads(response_body)
    else:
        print('error!')

def get_trans_text(text, target_lang):
    detect = detectLangs(text)
    if detect['langCode'] in trans_possible_lang_list:
        trans_text = translate(text, detect['langCode'], target_lang)
        return trans_text
    else:
        print('This is an untranslatable language. Please enter in another language.')