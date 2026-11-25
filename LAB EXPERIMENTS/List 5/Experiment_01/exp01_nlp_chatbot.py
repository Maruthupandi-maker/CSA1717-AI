"""
Experiment 01: Simple Chatbot using Natural Language Processing Techniques
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import re
import random

def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return set(text.split())

intents = {
    "greeting": {
        "keywords": {"hello", "hi", "hey", "greetings"},
        "responses": ["Hello! How can I assist you with AI today?", "Hi there! Ask me anything about CSA1717."]
    },
    "course": {
        "keywords": {"course", "subject", "csa1717", "ai", "artificial", "intelligence"},
        "responses": ["This is CSA1717 - Artificial Intelligence Lab at Saveetha School of Engineering."]
    },
    "nlp": {
        "keywords": {"nlp", "chatbot", "language", "tokenization"},
        "responses": ["NLP enables machines to understand, interpret, and generate human language."]
    },
    "bye": {
        "keywords": {"bye", "exit", "quit", "goodbye"},
        "responses": ["Goodbye! Happy coding!"]
    }
}

def chatbot_response(user_input):
    tokens = preprocess(user_input)
    best_intent = None
    max_overlap = 0
    for intent, data in intents.items():
        overlap = len(tokens.intersection(data["keywords"]))
        if overlap > max_overlap:
            max_overlap = overlap
            best_intent = intent
    if best_intent:
        return random.choice(intents[best_intent]["responses"])
    return "I'm sorry, I didn't understand that. Could you rephrase?"

if __name__ == "__main__":
    sample_inputs = ["Hello!", "Tell me about CSA1717 course", "What is NLP?", "Bye"]
    print("=== NLP Chatbot Simulation ===")
    for msg in sample_inputs:
        print(f"User: {msg}")
        print(f"Bot : {chatbot_response(msg)}\n")
