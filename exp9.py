from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

texts = [
    "I love this movie, it was fantastic", "Absolutely wonderful experience",
    "The food was delicious and fresh", "Great product, works perfectly",
    "I am very happy with the service", "Excellent quality and fast delivery",
    "The staff were friendly and helpful", "Superb story and brilliant acting",
    "I hate this movie, it was terrible", "Worst experience of my life",
    "The food was cold and tasteless", "Poor product, stopped working quickly",
    "I am very disappointed with the service", "Terrible quality and late delivery",
    "The staff were rude and unhelpful", "Awful story and dull acting",
]
labels = [1] * 8 + [0] * 8  # 1 = Positive, 0 = Negative

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42, stratify=labels)

vec = TfidfVectorizer()
Xtr, Xte = vec.fit_transform(X_train), vec.transform(X_test)

for name, model in [("Naive Bayes", MultinomialNB()), ("SVM", LinearSVC())]:
    model.fit(Xtr, y_train)
    pred = model.predict(Xte)
    print(f"\n===== {name} =====")
    print("Accuracy:", accuracy_score(y_test, pred))
    print(classification_report(y_test, pred, target_names=["Negative", "Positive"]))
