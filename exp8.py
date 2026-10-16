import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

for r in ['punkt', 'punkt_tab', 'wordnet', 'omw-1.4']:
    nltk.download(r, quiet=True)

# Part 1: Lesk WSD
sentences = [
    ("I went to the bank to deposit money.", "bank"),
    ("He used a bat to hit the ball.", "bat"),
    ("The mouse is connected to my computer.", "mouse"),
]

for s, w in sentences:
    sense = lesk(word_tokenize(s), w)
    print(f"\n{s}\n{w} -> {sense.name()}: {sense.definition()}")

# Part 2: Semantic relations
for w in ["good", "car", "tree", "dog", "bank"]:
    syn = wn.synsets(w)
    s = syn[0]
    print(f"\n--- {w.upper()} ---")
    print("Polysemy   :", len(syn))
    print("Synonyms   :", list({l.name() for x in syn for l in x.lemmas()})[:5])
    print("Antonyms   :", list({a.name() for x in syn for l in x.lemmas() for a in l.antonyms()}))
    print("Hypernyms  :", [h.name() for h in s.hypernyms()])
    print("Hyponyms   :", [h.name() for h in s.hyponyms()[:3]])
    print("Meronyms   :", [m.name() for m in s.part_meronyms() + s.member_meronyms()][:3])
