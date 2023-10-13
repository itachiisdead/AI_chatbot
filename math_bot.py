from chatterbot import ChatBot

bot=ChatBot("Math",logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("---------- Math Chatbot----------")

while True:
   user_ques=input("type the math equation that you want to solve: ")
   print("ChatBot: "+ str (bot.get_response(user_ques)))