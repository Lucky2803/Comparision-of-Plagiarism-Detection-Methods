import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
import string
import re
import rabin_karp
from os.path import dirname, join



class PlagiarismChecker:
    def __init__(self, file_a, file_b):
        self.file_a = file_a
        self.file_b = file_b
        self.hash_table = {"a": [], "b": []}
        self.k_gram = 5
        content_a = self.get_file_content(self.file_a)
        content_b = self.get_file_content(self.file_b)
        self.calculate_hash(content_a, "a")
        self.calculate_hash(content_b, "b")

    # calculate hash value of the file content
    # and add it to the document type hash table
    def calculate_hash(self, content, doc_type):
        text = self.prepare_content(content)
        text = "".join(text)


        text = rabin_karp.rolling_hash(text, self.k_gram)
        for _ in range(len(content) - self.k_gram + 1):
            self.hash_table[doc_type].append(text.hash)
            if text.next_window() == False:
                break


    def get_rate(self):
        return self.calaculate_plagiarism_rate(self.hash_table)

    # calculate the plagiarism rate using the plagiarism rate formula
    def calaculate_plagiarism_rate(self, hash_table):
        th_a = len(hash_table["a"])
        th_b = len(hash_table["b"])
        a = hash_table["a"]
        b = hash_table["b"]
        sh = len(np.intersect1d(a, b))
        # print(sh, a, b)
        # print(sh, th_a, th_b)

        # Formular for plagiarism rate
        # P = (2 * SH / THA * THB ) 100%
        p = (float(2 * sh)/(th_a + th_b)) * 100
        return p

    # get content from file
    def get_file_content(self, filename):
        file = open(filename, 'r+', encoding="utf-8")
        return file.read()

    def prepare_content(self, content):
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


current_dir = dirname(__file__)
checker = PlagiarismChecker(
    join(current_dir, "Source.txt"),
    join(current_dir, "Test.txt")
)

