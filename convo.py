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


list_to_train=[
 "what's your name ",
 "I'm BeepBop",
 "how old are you?",
 "I do not have an age. However I was created by Heba Maher in october,2023",
 "who made you?",
 "Heba Maher created me in october,2023",
]

trainer = ChatterBotCorpusTrainer(beepbop)
trainer.train("chatterbot.corpus.english")

list_trainer =ListTrainer(beepbop)
list_trainer.train(list_to_train)

print("what is your name? ")
user_name =input()

@app.route("/")
def main():
  return render_template("index.html")



while True:
  user_response=input(user_name+": ")
  print("BeepBop: "+ str(beepbop.get_response(user_response)))


  if __name__ =="__main__":
    app.run(depug=True) 