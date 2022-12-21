# Plagiarism-Detector-String-Matching-

The project presents comparision among various methods to design a text similarity checker that checks for plagiarsim between two text documents (Source and Test) by using:<br /> <br />
Jaccard Similarity,<br />
Cosine Similarity,<br />
Eucledian Distance and a<br />
Custom Rabin Karp Algorithm inspired method. <br />

NLP has been used to clean (removing stopwords, punctuations, URLs etc.), stem (Porter Stemmer) and tokenize the text before the initationg the similarity detection process.<br />

Rabin Karp Algortihm is the preferred choice for this project as it is based on hashing and the percentage of plagiarism can be scaled accordingly by generating and comparing hash values for the entire text. An accuarcy comparision has been made among the 4 methods.
In the future, it is planned to incorporate Levenshtein Distance in combination with Rabin Karp alogrithm to imporve the accuracy of the checker.<br />

Python Files: <br />
Main: for running all plag checks <br />
Filtertext: To clean content (Data Pre Processing) before passing data to functions. <br />
KarpSimiliarityCheck: For defining the custom plag detection class. <br />
RabinKarp: For implementing the rabin karp string matching algorithm. <br />

Txt files:<br />
Source: conatins the source document. <br />
Test: conatins content similar to source file. <br />

References:<br />

https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf <br /></br />
https://www.researchgate.net/publication/316681173_Text_Documents_Plagiarism_Detection_using_Rabin-Karp_and_Jaro-Winkler_Distance_Algorithms <br />
