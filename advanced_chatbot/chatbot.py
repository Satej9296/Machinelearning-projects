import json
import pickle
import random
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')

# Load intents
with open("intents.json") as file:
    intents = json.load(file)

def clean_text(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def chatbot_response(user_input):
    cleaned = clean_text(user_input)
    vector = vectorizer.transform([cleaned])
    tag = model.predict(vector)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

print("🤖 Advanced AI Chatbot is running (type 'quit' to stop)\n")

while True:
    user = input("You: ")
    if user.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break
    response = chatbot_response(user)
    print("Bot:", response)
