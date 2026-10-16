# Name: Kushal Dubey
# Roll No: TEA113

import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

print("Name: Kushal Dubey")
print("Roll No: TEA113\n")

# Input sentence
sentence = "Kushal Dubey studies at LTCOE. He also plays cricket."

# Tokenization
words = nltk.word_tokenize(sentence)
print("Tokens:")
print(words)

# Part-of-speech tagging
pos_tags = nltk.pos_tag(words)
print("\nPOS Tags:")
print(pos_tags)

# Extract nouns and verbs
nouns = []
verbs = []

for word, tag in pos_tags:
    # Nouns: NN, NNS, NNP, NNPS
    if tag.startswith('NN'):
        nouns.append(word)
    # Verbs: VB, VBD, VBG, VBN, VBP, VBZ
    elif tag.startswith('VB'):
        verbs.append(word)

print("\nNouns:")
print(nouns)

print("\nVerbs:")
print(verbs)
