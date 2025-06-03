from flask import Flask, request, render_template
from chatbot import simple_chatbot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_input = request.form["query"]
        reply = simple_chatbot(user_input)
    return render_template("index.html", response=reply)

if __name__ == "__main__":
    app.run(debug=True)
