import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
import string
import re


def filter_content(content):
    # STOP WORDS
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(content)

    filtered_content = []
    # STEMMING
    stemmer = PorterStemmer()
    for w in word_tokens:
        # Cleaning Data

        if w not in stop_words:
            # Change everything to lowercase
            w = w.lower()
            # remove unicode characters
            w = w.encode('ascii', 'ignore').decode()
            # remove mentions e.g.: @Lakshay
            w = re.sub("@\S+", " ", w)
            # remove URLs
            w = re.sub("https*\S+", " ", w)
            # remove hastags
            w = re.sub("#\S+", " ", w)
            # remove punctuations
            w = re.sub('[%s]' % re.escape(string.punctuation), ' ', w)
            # remove overspaces
            w = re.sub('\s{2,}', " ", w)
            # stemmer
            word = stemmer.stem(w)
            filtered_content.append(word)

    return filtered_content