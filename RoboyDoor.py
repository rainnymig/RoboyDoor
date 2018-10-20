import sys
import time
import telepot
import random
from os import listdir
from os.path import join, dirname, isfile, realpath
from telepot.loop import MessageLoop
from pprint import pprint
from playsound import playsound

BotAuthCode = "741304853:AAEC9t__AwP_75_lEQOlSOq6H7KXDjE404s"

ChatTitles = ["Roboy Core Team", "开门啊"]

RoboyOpenDoorSticker = "CAADAgADcwAD5dCAEEsvdJvjUpsSAg"

AudioDir = dirname(realpath(__file__))
AudioDir = join(AudioDir, "audios")

DoorOpenerIp = "192.168.0.137"

audioFiles = [f for f in listdir(AudioDir) if isfile(join(AudioDir, f))]
l = range(0, len(audioFiles))

def handle(msg):
	contentType, chatType, chatId = telepot.glance(msg)
	if (chatType == "group" and (msg["chat"]["title"] in ChatTitles)):
		if contentType == "sticker" and msg["sticker"]["file_id"] == RoboyOpenDoorSticker:
			playsound(join(AudioDir, audioFiles[random.choice(l)]))

bot = telepot.Bot(BotAuthCode)
MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(10)
