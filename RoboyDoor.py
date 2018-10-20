import sys
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
from playsound import playsound

BotAuthCode = "741304853:AAEC9t__AwP_75_lEQOlSOq6H7KXDjE404s"

ChatTitles = ["Roboy Core Team", "开门啊"]

RoboyOpenDoorSticker = "CAADAgADcwAD5dCAEEsvdJvjUpsSAg"

DoorOpenerIp = "192.168.0.137"

def handle(msg):
	contentType, chatType, chatId = telepot.glance(msg)
	if (chatType == "group" and (msg["chat"]["title"] in ChatTitles)):
		if contentType == "sticker" and msg["sticker"]["file_id"] == RoboyOpenDoorSticker:
			playsound('audios/canopenthedoor.mp3')


bot = telepot.Bot(BotAuthCode)
MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(10)
