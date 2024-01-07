import re
import asyncio
import telegram
from flask import Flask, request
from credentials import bot_token

async def main():
   bot = telegram.Bot(bot_token)
   app = Flask(__name__)
   # retrieve the message in JSON and then transform it to Telegram object
   updates = (await bot.get_updates())
   update = updates[len(updates) - 1]

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()

   # for debugging purposes only
   print("got text message :", text)

   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = "Welcome to TestBot"
       # send the welcoming message
       await bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
   else:
       try:
           # clear the message we got from any non alphabets
           text = re.sub(r"\W", "_", text)
           await bot.sendMessage(chat_id=chat_id, text="test Message", reply_to_message_id=msg_id)
       except Exception:
           # if things went wrong
           await bot.sendMessage(chat_id=chat_id, text="There was a problem", reply_to_message_id=msg_id)

    # async with bot:
    #     # updates = (await bot.get_updates())
    #     # for _ in updates:
    #     #     print(_.message.text)
    #     await bot.send_message(text='Hi KYLE!!', chat_id=151717390)


if __name__ == '__main__':
    asyncio.run(main())
