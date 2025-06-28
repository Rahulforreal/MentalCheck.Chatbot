from flask import Flask, render_template, request
from transformers import pipeline, set_seed

app = Flask(__name__)

# ✅ Use a lightweight model that fits within 512Mi RAM
chatbot = pipeline("text-generation", model="distilgpt2")
set_seed(42)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = chatbot(user_input, max_length=100, pad_token_id=50256)
        response = result[0]['generated_text']
    return render_template("index.html", response=response)

@app.route("/ping")
def ping():
    return "pong"
