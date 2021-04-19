from helper import remove_punc
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string
import numpy as np

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    with open(doc) as f:
        f_read = f.read()
        data = f_read.splitlines()
        
    #2. Tokenize string using nltk.tokenize.word_tokenize

    doc_tokens = [nltk.tokenize.word_tokenize(x) for x in data]
    
    #3. Filter out punctuation from list of words (use remove_punc)

    doc_nopunc = [remove_punc(a_doc) for a_doc in doc_tokens]

    #4. Make the words lower case
    doc_lower = [[x.lower() for x in doc_a] for doc_a in doc_nopunc]
    
    #5. Filter out stopwords

    stop = stopwords.words('english')
    doc_tokens_clean = [[x.lower() for x in words if x.lower() not in stop] for words in doc_lower]
    doc_filtered = [x for x in doc_tokens_clean if x]
    
    #6. Stem words
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    doc_tokens_clean_lem = [[stemmer.stem(x) for x in words] for words in doc_filtered]
    
    words_list = []
    for s in doc_tokens_clean_lem:
        for x in s:
            words_list.append(x)

    words_list = [w for w in words_list]
    
    f.close()
    return words_list
    
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



    words = [readAndCleanDoc(i) for i in doclist]

    set_word = set()

    for word in words:
        set_word.update(word)

    words_list = list(set_word)

    words_list = sorted(words_list)



    #2. Use these word lists to build the doc word matrix

    #

    docword = np.zeros((len(doclist),len(words_list)))

    for ind,word in enumerate(words):
        for i in word:
            ######

            docword[ind,words_list.index(i)] = docword[ind,words_list.index(i)] + 1;
            
    

    return docword, words_list
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    #print(docword)

    tf = [i/np.sum(i) for i in docword]
    
    tf = np.array(tf)
    #tf = docword/sum_doc

    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in
    sum_col = np.sum(docword,axis=0)
    #sum_array = [0]*len(sum_col)
    count_array = [0]*sum_col.size
    if len(docword) > 1:
        for i in docword:
            count = 0
            for k in i:
            #sum_array[count] += k
                if k != 0:
                    count_array[count] += 1
                count += 1

    else:
        count_array = [1]*sum_col.size
    #print(sum_col)
    #print(count_array)
    idf = np.array([])
    n1 = np.ones((1,len(sum_col)))
    sum_col1 = sum_col*n1
    idf = np.log10(len(docword)/np.array(count_array))
    idf = idf*n1

    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in
    idf = buildIDFMatrix(docword)

    tf = [i/np.sum(i) for i in docword]
    
    tf = np.array(tf)

    tfidf = tf * idf

    
    
    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    length = len(doclist)
    for i in range(length):

        tfidf = buildTFIDFMatrix(docword)

        dist_words = np.argsort(-tfidf[i,:])[:3]

        distinctiveWords[doclist[i]] = list(np.array(wordlist)[dist_words])
    
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
    ''''
    #Uncomment and recomment ths part where you see fit for testing purposes
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
    '''
