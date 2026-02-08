import json
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json") as file:
    data = json.load(file)

sentences = []
labels = []

# NLP preprocessing
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = word_tokenize(pattern.lower())
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        sentences.append(" ".join(tokens))
        labels.append(intent["tag"])

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

# Train ML model
model = LogisticRegression()
model.fit(X, labels)

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("AI model trained successfully!")
