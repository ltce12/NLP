import nltk

for r in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng']:
    nltk.download(r, quiet=True)

tags = {
    "CC": "Coordinating conjunction", "CD": "Cardinal number", "DT": "Determiner",
    "EX": "Existential there", "FW": "Foreign word", "IN": "Preposition/subordinating conj.",
    "JJ": "Adjective", "JJR": "Adjective, comparative", "JJS": "Adjective, superlative",
    "LS": "List item marker", "MD": "Modal", "NN": "Noun, singular", "NNS": "Noun, plural",
    "NNP": "Proper noun, singular", "NNPS": "Proper noun, plural", "PDT": "Predeterminer",
    "POS": "Possessive ending", "PRP": "Personal pronoun", "PRP$": "Possessive pronoun",
    "RB": "Adverb", "RBR": "Adverb, comparative", "RBS": "Adverb, superlative",
    "RP": "Particle", "SYM": "Symbol", "TO": "To", "UH": "Interjection",
    "VB": "Verb, base form", "VBD": "Verb, past tense", "VBG": "Verb, gerund/present participle",
    "VBN": "Verb, past participle", "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present", "WDT": "Wh-determiner", "WP": "Wh-pronoun",
    "WP$": "Possessive wh-pronoun", "WRB": "Wh-adverb", "#": "Hash", "$": "Dollar",
    ".": "Sentence terminator", ",": "Comma", ":": "Colon", "``": "Opening quote",
    "''": "Closing quote", "-LRB-": "Left bracket", "-RRB-": "Right bracket", "--": "Dash"
}

print("===== POS TAGS =====")
for t, m in tags.items():
    print(f"{t:6}: {m}")

sentence = input("\nEnter a sentence: ")

print("\n===== POS TAGGING RESULT =====")
for w, t in nltk.pos_tag(nltk.word_tokenize(sentence)):
    print(f"{w:15} {t:6} {tags.get(t, 'Unknown')}")
