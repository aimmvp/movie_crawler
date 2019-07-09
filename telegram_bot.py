import telegram
import mykey

telegram_key = mykey.TELEGRAM_KEY
bot = telegram.Bot(token =  telegram_key)
# for i in bot.getUpdates():
#     print(i.message)

# print(bot.get_me())
bot.sendMessage(chat_id = 848365857, text="테스트입니다.")