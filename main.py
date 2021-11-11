import telepot, json, time
from telepot.loop import MessageLoop
from chatbot import Maria

with open('token.json') as jsonFile:
    token = json.load(jsonFile)
telegram = telepot.Bot(token)
bot = Maria("Maria_Bot")

def receiveMsg(msg):
    frase = bot.listen(phrase=msg['text'])
    response = bot.think(frase)
    bot.speak(response)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, response)

MessageLoop(telegram, receiveMsg).run_as_thread()
print ('success')

while True:
    time.sleep(10)
