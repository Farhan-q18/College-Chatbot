import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as file:
    data = json.load(file)

texts = []
labels = []

# Prepare training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression(max_iter = 1000)
model.fit(X, labels)

# Predict intent
def predict_intent(user_input):
    X_test = vectorizer.transform([user_input])
    probs = model.predict_proba(X_test)
    
    confidence = max(probs[0])
    tag = model.predict(X_test)[0]

    return tag, confidence

# Get response
def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    
    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    while True:
        msg = input("You: ")
        tag, _ = predict_intent(msg)
        print("Bot:", get_response(tag))