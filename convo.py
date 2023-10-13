from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot0=ChatBot("chatbot",read_only=False,
             logic_adapters=[
               {
               "import_path":"chatterbot.logic.BestMatch",
               "default_response":"sorry I don't have an answer",
               "maximum_similarity_threshold":0.9
               }
               ])


trainer = ChatterBotCorpusTrainer(bot0)
trainer.train("chatterbot.corpus.english")


print("what is your name? ")
user_name =input()

while True:
  user_response=input(user_name+": ")
  print("vera: "+ str(bot0.get_response(user_response))) 