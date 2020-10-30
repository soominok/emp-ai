from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
import numpy as np
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class UserData:
    def __init__(self):
        self.okt = Okt()

    def read_file(self):
        self.okt.pos("morph", stem=True)
        cheese_data = pd.read_csv("com_cheese_api/user/data/users.csv")
        cheese_lists = list(cheese_data['cheese_name'])
        tests = ''.join(cheese_lists)
        #print(cheese_str)
        #print(type(cheese_str))
        return texts
        

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        return tokens

    def extract_noun(self):
        noun_tokens = []
        tokens = self.change_token(self.extract_hangeul(self.read_file()))
        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))
        texts = " ".join(noun_tokens)
        return texts


    @staticmethod
    def download():
        nltk.download()

    @staticmethod
    def read_stopword():
        with open('com_cheese_api/user/data/stopword.txt', 'r') as file:
            lines = file.readlines()
            stop_str = ''.join(lines)
            stopword = stop_str.replace('\n', ' ')
            stopwords = stopword.split(' ')
        return stopwords       


    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        stopwords = self.read_stopword()
        texts = [text for text in tokens
                    if text not in stopwords]
        return texts


    def hook(self):
        texts = self.remove_stopword()
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:100])
        return freqtxt


    def draw_wordcloud(self):
        texts = self.remove_stopword()
        wcloud = WordCloud('/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf', background_color='white', width=800, height=600)
        cloud = wc.generate_from_frequencies(dict(tags))
        plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(cloud)
        plt.show()

UserData()
