from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask,render_template

app=Flask(__name__)

beepbop=ChatBot("chatbot",read_only=False,
             logic_adapters=[
               {
               "import_path":"chatterbot.logic.BestMatch",
               "default_response":"sorry I don't have an answer",
               "maximum_similarity_threshold":0.9
               }
               ])


trainer = ChatterBotCorpusTrainer(beepbop)
#trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
   return render_template("index.html")



#while True:
#  user_response=input("User: ")
#  print("BeepBop: "+ str(beepbop.get_response(user_response)))


if __name__ =="__main__":
     app.run(debug=True) 