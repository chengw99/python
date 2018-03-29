# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:54:52 2018

@author: chen
"""

from wordcloud import WordCloud
import jieba
from scipy.misc import imread
from os import path
import matplotlib.pyplot as plt
from PIL import Image

def draw_wordcloud():
    comment_text = open(u'D:\python\chinese.txt',encoding='gbk',errors='ignore').read()
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__)
    font_path = 'simkai.ttf'
    #color_mask = imread('test.png')
    cloud = WordCloud(
            font_path=font_path,
            background_color='white',
            #mask=color_mask,
            max_words=2000,
            max_font_size=40
    )
    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file('1.png')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    
if __name__ == '__main__':
    draw_wordcloud()