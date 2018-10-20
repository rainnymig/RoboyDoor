import sys
import time
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('imcoming: %s\n' % command)



bot = telepot.Bot('741304853:AAEC9t__AwP_75_lEQOlSOq6H7KXDjE404s')
bot.message_loop(handle)
print('I am listening')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\nProgram interrupt, exit.\n')
        exit()

    except:
        print('\nOther error\n')
        exit()
