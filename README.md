# Plagiarism-Detector-String-Matching-

The project presents comparision among various methods to design a text similarity checker that checks for plagiarsim between two text documents (Source and Test) by using 
Jaccard Similarity,
Cosine Similarity,
Eucledian Distance and a
Custom Rabin Karp Algorithm inspired method. 

NLP has been used to clean (removing stopwords, punctuations, URLs etc.), stem (Lancaster Stemmer) and tokenize the text before the initationg the similarity detection process.

Rabin Karp Algortihm is the preferred choice for this project as it is based on hashing and the percentage of plagiarism can be scaled accordingly by generating and comparing hash values for the entire text. An accuarcy comparision has been made among the 4 methods.
In the future, it is planned to incorporate Levenshtein Distance in combination with Rabin Karp alogrithm to imporve the accuracy of the checker.

Python Files:
Main: for running all plag checks 
Filtertext: To clean content (Data Pre Processing) before passing data to functions. 
KarpSimiliarityCheck: For defining the custom plag detection class. 
RabinKarp: For implementing the rabin karp string matching algorithm. 

Txt files:
Source: conatins the source document. 
Test: conatins content similar to source file. 

