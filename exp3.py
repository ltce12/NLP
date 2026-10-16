#Stemming program
# Import stemmers
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

# Create stemmer objects
porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()

# Sample words
words = [
    "playing", "played", "playing",
    "studies", "studying", "running",
    "happiness", "connected",
    "connection", "relational",
    "children", "better"
]

# Print heading
print("{:<15} {:<15} {:<15} {:<15}".format(
    "Original", "Porter", "Snowball", "Lancaster"))
print("-" * 60)

# Apply all stemmers
for word in words:
    print("{:<15} {:<15} {:<15} {:<15}".format(
        word,
        porter.stem(word),
        snowball.stem(word),
        lancaster.stem(word)
    ))



#______________________________________________________

  #Lemmatization using nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["playing", "studies", "running", "cars", "children", "mice"]

print(f"{'Word':<15}{'Lemma':<15}")
print("-" * 30)

for word in words:
    print(f"{word:<15}{lemmatizer.lemmatize(word):<15}")
    

#______________________________________________

#Lemmatization using Spacy
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

words = ["playing", "studies", "running", "cars", "children", "mice"]

print(f"{'Word':<15}{'Lemma':<15}")
print("-" * 30)

for word in words:
    doc = nlp(word)
    print(f"{word:<15}{doc[0].lemma_:<15}")

#__________________________________________________
