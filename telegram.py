import telepot, json, time
from telepot.loop import MessageLoop

with open ("token.json") as jsonFile: 
    token = json.load (jsonFile)

bot = telepot.Bot(token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, "Que bom te ver por aqui!")


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)