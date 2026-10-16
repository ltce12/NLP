# Import required libraries
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Download required data
nltk.download('punkt')
nltk.download('punkt_tab')


# Function for Unigram
def unigram_model(text):
    tokens = word_tokenize(text.lower())
    unigrams = list(ngrams(tokens, 1))
    print("\nUnigrams:")
    for gram in unigrams:
        print(gram)


# Function for Bigram
def bigram_model(text):
    tokens = word_tokenize(text.lower())
    bigrams = list(ngrams(tokens, 2))
    print("\nBigrams:")
    for gram in bigrams:
        print(gram)


# Function for Trigram
def trigram_model(text):
    tokens = word_tokenize(text.lower())
    trigrams = list(ngrams(tokens, 3))
    print("\nTrigrams:")
    for gram in trigrams:
        print(gram)


# Function for 5-Gram
def fivegram_model(text):
    tokens = word_tokenize(text.lower())
    fivegrams = list(ngrams(tokens, 5))
    print("\n5-Grams:")
    for gram in fivegrams:
        print(gram)


# Main Program
text = input("Enter a sentence: ")

unigram_model(text)
bigram_model(text)
trigram_model(text)
fivegram_model(text)
