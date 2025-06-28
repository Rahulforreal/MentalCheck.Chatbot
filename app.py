from flask import Flask, render_template, request
from transformers import pipeline, set_seed

app = Flask(__name__)

# Use text-generation instead of conversational
chatbot = pipeline("text-generation", model="distilgpt2")


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        full_input = f"User: {user_input} \nBot:"
        result = chatbot(full_input, max_length=100, pad_token_id=50256)
        response = result[0]['generated_text'].split("Bot:")[-1].strip()
    return render_template("index.html", response=response)

@app.route("/ping")
def ping():
    return "pong"



