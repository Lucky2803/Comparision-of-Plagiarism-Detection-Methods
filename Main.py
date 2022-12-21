import KarpSimilarityChecker
import spacy
import Filtertext
from pathlib import Path
from collections import Counter
from math import*
import re
WORD = re.compile(r"\w+")


a = Path('Source.txt').read_text()
b = Path('Test.txt').read_text()

from Filtertext import filter_content

Source = filter_content(a)
Test = filter_content(b)


src = ""
for i in Source:
    src = src + i + " "

#remove overspaces
src = re.sub('\s{2,}', " ", src)

# print(src)

tst = ""
for i in Test:
    tst = tst + i + " "

#remove overspaces
tst = re.sub('\s{2,}', " ", tst)
# print(tst)


#Custom Plagiarism detector
from KarpSimilarityChecker import checker
print("Custom Plag detctor: ", str(round(checker.get_rate(),2)) ,'%')


#Jaccard Similarity
#Jaccard similarity = overlaps/total  = len of intersection/len of union

def jaccard_similarity(x,y):
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)

print("Jaccard Similarity: ", str(round(jaccard_similarity(Source, Test)*100,1)), "%")



# Cosine Similarity

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = sqrt(sum1) * sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

vec1 = text_to_vector(src)
vec2 = text_to_vector(tst)

cosine = get_cosine(vec1, vec2)
print("Cosine Similarity: ",str(round(cosine*100,1)), "%")

# aliter

# from sklearn.feature_extraction.text import TfidfVectorizer

# # Create an instance of the TfidfVectorizer

# vectorizer = TfidfVectorizer()
# corpus = [src,tst]

# # Fit the vectorizer to the text data
# trsfm  = vectorizer.fit_transform(corpus)
#
# from sklearn.metrics.pairwise import cosine_similarity
# similarity = cosine_similarity(trsfm[0],trsfm)
#
# print("Cosine Similarity: ",str(round(similarity[0][1],2)*100), "%")


#Eucledian Similarity

# Line 1: Define the euclidean_distance function and specify the input arguments x and y
def euclidean_distance(x, y):
    # Line 2: Calculate the Euclidean distance between x and y using a generator expression
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

# Line 3: Create a list of sentences
sentences = [src, tst]

# Line 4: Load a pre-trained spaCy model
nlp = spacy.load('en_core_web_md')

# Line 5: Create a list of embeddings for the sentences using the spaCy model
embeddings = [nlp(sentence).vector for sentence in sentences]

# Line 6: Calculate the Euclidean distance between the first two embeddings
distance = euclidean_distance(embeddings[0], embeddings[1])

# Line 7: Define the distance_to_similarity function and specify the input argument distance
def distance_to_similarity(distance):
  # Line 8: Convert the distance to a similarity score using the formula 1/exp(0.45*distance)
  return 1/exp(0.45*distance)



print("Eucledian Distance Approximation: ",str(round(distance_to_similarity(distance)*100,1)), "%")
