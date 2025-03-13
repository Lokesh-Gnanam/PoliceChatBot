from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined intents dataset
intents = {
    "intents": [
        {"tag": "lost_phone", "patterns": ["I lost my phone", "My phone is missing", "I can't find my phone"], "responses": ["Can you provide the last known location?", "Did you check your recent activities?"]},
        {"tag": "cybercrime", "patterns": ["I was scammed", "My account was hacked", "I got a phishing email"], "responses": ["Please report it immediately to the cybercrime division. Do you need contact details?"]},
    ]
}

def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "Sorry, I couldn't understand. Can you please elaborate?"

@app.route("/")  
def home():
    return render_template("index.html")  # Loads the HTML file

@app.route("/get_response", methods=["POST"])
def respond():
    user_input = request.json.get("user_input")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
