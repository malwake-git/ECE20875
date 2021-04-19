from helper import remove_punc
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
#nltk.download('punkt')


#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc):
    #1. Open document, read text into *single* string
    f = open(doc)
    data = f.read()
    list_docs = data.splitlines()
    #2. Tokenize string using nltk.tokenize.word_tokenize
    token_doc = [nltk.tokenize.word_tokenize(x) for x in list_docs]
    #3. Filter out punctuation from list of words (use remove_punc)
    token_punc = [remove_punc(word) for word in token_doc]

    #4. Make the words lower case
    token_lower = []

    for line in token_punc:
        sub_lst = []

        for word in line:
            low_word = word.lower()
            sub_lst.append(low_word)
        token_lower.extend(sub_lst)

    #5. Filter out stopwords
    #nltk.download('stopwords')
    stops = stopwords.words('english')
    token_stop = [x for x in token_lower if x not in stops]

    #6. Stem words
    #nltk.download('wordnet')
    stemmer = PorterStemmer()
    words = []
    for word in token_stop:
        words.append(stemmer.stem(word))
    f.close()
    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordlist = []
    for doc in doclist:
        for word in doc:
            if (not(word in wordlist)):
                wordlist.append(readAndCleanDoc(doc))
    #print(wordlist)
    # 2. Use these word lists to build the doc word matrix
    docword = []
    print(wordlist[2])
    for doc in wordlist:
        #print(doc)
        doc_vec = [0] * len(wordlist)
        #print(doc_vec)
        for word in doc:
            #print(word)
            if word in wordlist:
                ind = wordlist.index(word)
                doc_vec[ind] += 1
                docword.extend(doc_vec)
        #print(doc_vec)
    #print(docword)

    # Check that this produces the same result
    ##np.all(np.isclose(doc_word, doc_word_simple))
    return docword, wordlist

#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    #term_freq = [i / np.sum(i) for i in docword]
    #tf = np.array(tf)

    #return tf

    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in


    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in



    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html

    
    
    return distinctiveWords


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes

    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***") 
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))

