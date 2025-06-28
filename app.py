from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

chatbot = None  # Delay loading to avoid timeout

@app.before_first_request
def load_model():
    global chatbot
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route("/", methods=["GET", "POST"])
def index():
    global chatbot
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if chatbot is None:
            load_model()  # Load if not already loaded
        result = chatbot(user_input)
        response = result[0]['generated_responses'][0]
    return render_template("index.html", response=response)

@app.route("/ping")
def ping():
    return "pong"  # Useful for Render health check

# No if __name__ == "__main__" block here

