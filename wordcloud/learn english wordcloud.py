# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:30:41 2018

@author: DELL
"""
from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

f = open(r'e:\py_data\best.txt','r').read()

alice_mask = np.array(Image.open(r'e:\py_data\alice.png'))
stopwords = set(STOPWORDS)
stopwords.add('python')

wordcloud = WordCloud(background_color='white',mask=alice_mask,width=1000,height=860,margin=2,stopwords=stopwords).generate(f)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()