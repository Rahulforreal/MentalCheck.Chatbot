from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = chatbot(user_input)
        response = result[0]['generated_responses'][0]
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

