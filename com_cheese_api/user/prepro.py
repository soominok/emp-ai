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
        cheese_df = cheese_data.loc[:,['cheese_name']]
        texts = np.array(cheese_df['cheese_name'].tolist())
        return texts
        

    @staticmethod
    def make_wordcloud(word_count):
    okt = Okt()
    
    sentences_tag = []
    
    #형태소 분석하여 리스트에 넣기
    for sentence in cheese_lists:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        #print(morph)
        #print('-' * 30)
    
    #print(sentences_tag)
    #print('\n' * 3)
    
    noun_adj_list = []
    #명사와 형용사만 구분하여 이스트에 넣기
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                if len(word) >= 2:
                    noun_adj_list.append(word)
                    
    
    word_count_list = []
    #형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    word_count_list.append(tags)
    word_list = sum(word_count_list, [])
    #print(word_list)

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

if __name__ == '__main__':
    UserData()
