from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
import numpy as np
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class CheeseData:
    def __init__(self):
        self.okt = Okt()

    @staticmethod
    def read_file(self):
        cheese_data = pd.read_csv("com_cheese_api/user/data/users.csv")
        cheese_df = cheese_data.loc[:,['cheese_name']]
        texts = np.array(cheese_df['cheese_name'].tolist())
        return texts
        print('-' * 10)
        print(texts)

    def extract_hangeul(self):
        #temp = texts.replace('\n', ' ')
        sentences_tag = []
        for sentence in texts:
            morph = self.okt.pos(sentence)
            sentences_tag.append(morph)
        return sentences_tag

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
        stopfile = 'com_cheese_api/user/data/stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
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
        print(freqtxt[:30])
        return freqtxt


    def draw_wordcloud(self):
        texts = self.remove_stopword()
        wcloud = WordCloud('/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf', relative_scaling=0.2,
                           background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    CheeseData()