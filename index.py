from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a ChatBot instance
chatbot = ChatBot("My ChatBot")

# Create a trainer and train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Define a route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Define a route for getting the chatbot response
@app.route("/get_chatbot_response", methods=["POST"])
def get_chatbot_response():
    user_message = request.form["user_message"]
    response = chatbot.get_response(user_message)
    return str(response)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)