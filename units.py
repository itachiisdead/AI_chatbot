from chatterbot import ChatBot

bot=ChatBot("units",logic_adapters=["chatterbot.logic.UnitConversion"])

while True:
    user_text=input("use unit conversion: ")
    ChatBot_response = str(bot.get_response(user_text))
    print(ChatBot_response )