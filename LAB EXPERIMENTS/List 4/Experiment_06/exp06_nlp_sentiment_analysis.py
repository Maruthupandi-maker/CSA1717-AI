"""
Experiment 06: Sentiment Analysis using Natural Language Processing (NLP) Techniques
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = [
    "This AI course is fantastic and very informative",
    "Great explanation of machine learning algorithms",
    "I loved the practical lab exercises",
    "Terrible experience and confusing documentation",
    "The software crashed and wasted my time",
    "Poor quality and very disappointing results"
]
labels = [1, 1, 1, 0, 0, 0]  # 1 = Positive, 0 = Negative

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(reviews)

model = MultinomialNB()
model.fit(X_train, labels)

test_sentences = [
    "The lab exercises are great and informative",
    "Confusing code and poor results"
]
X_test = vectorizer.transform(test_sentences)
preds = model.predict(X_test)

print("=== NLP Sentiment Analysis (Naive Bayes) ===")
for text, label in zip(test_sentences, preds):
    sentiment = "Positive" if label == 1 else "Negative"
    print(f"Text: '{text}' -> Sentiment: {sentiment}")
