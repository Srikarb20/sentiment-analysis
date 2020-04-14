# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:30:24 2020

@author: srika
"""

#importing libraries
from textblob import TextBlob
import nltk
from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#getting the article
url='https://everythingcomputerscience.com'
article=Article(url)
#using NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
#getting summary of the article
text=article.summary
def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub('#', '', text) # Removing '#' hash tag
 text = re.sub('RT[\s]+', '', text) # Removing RT
 text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
 return text
#print the text
print(text)
#creating a text blob object
obj=TextBlob(text)
#this returns a value between -1 and 1
sentiment=obj.sentiment.polarity
print(sentiment)
if sentiment==0:
    print("Text is neutral")
elif sentiment>0:
    print("Text is positive")
else:
    print("Text is negative")
    #using word cloud
wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(text)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()

