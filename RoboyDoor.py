import sys
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
from playsound import playsound

ChatTitle = ["Roboy Core Team", "开门啊"]

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if (chat_type == "group" and (msg["chat"]["title"] in ChatTitle)):
		if content_type == "sticker":
			bot.sendMessage(chat_id, "you send a message")
			playsound('audios/canopenthedoor.mp3')


bot = telepot.Bot('741304853:AAEC9t__AwP_75_lEQOlSOq6H7KXDjE404s')
MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(10)
