from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot0=ChatBot("chatbot",read_only=False,logic_adapters=["chatterbot.logic.BestMatch"])

list_to_train=[
 "hi",
 "hey there!",
 "what's your name ",
 "I'm vera",
 "how old are you?",
 "I am a chatbot and do not have an age. However I was created by Heba Maher in october,2023",
 "what can you do?",
 "I am a simple general purpose chatbot that can tell jokes as well",
 "tell me a joke",
 "Where do fish keep their money?   In a river bank. "

]

list_trainer =ListTrainer(bot0)

list_trainer.train(list_to_train)
print("what is your name? ")
user_name =input()

while True:
  user_response=input(user_name+": ")
  print("vera: "+ str(bot0.get_response(user_response)))
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask,render_template

app=Flask(_name_)

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
 # user_response=input("User: ")
  #print("BeepBop: "+ str(beepbop.get_response(user_response)))


  if _name_ =="_main_":
    app.run(depug=True)