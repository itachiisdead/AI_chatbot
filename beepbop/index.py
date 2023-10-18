from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests 
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
    rawdata=requests.get("https://api.openweathermap.org/data/2.5/weather?q=cairo&appid=8a5f0459dbfb397e81ac7d506b5e648f")
    result=rawdata.json()
    return str(result)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)