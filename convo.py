from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


beepbop=ChatBot("chatbot",read_only=False,
             logic_adapters=[
               {
               "import_path":"chatterbot.logic.BestMatch",
               "default_response":"sorry I don't have an answer",
               "maximum_similarity_threshold":0.9
               }
               ])


list_to_train=[
 "hi",
 "hey there!",
 "what's your name ",
 "I'm BeepBop",
 "how old are you?",
 "I am a chatbot and do not have an age. However I was created by Heba Maher in october,2023",
 "what can you do?",
 "I am a simple general purpose chatbot that can tell jokes as well",
 "who made you?",
 "Heba Maher created me in october,2023",
 
]

list_trainer =ListTrainer(beepbop)
list_trainer.train(list_to_train)

trainer = ChatterBotCorpusTrainer(beepbop)
trainer.train("chatterbot.corpus.english")


print("what is your name? ")
user_name =input()

while True:
  user_response=input(user_name+": ")
  print("BeepBop: "+ str(beepbop.get_response(user_response))) 