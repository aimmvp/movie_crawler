import telegram

bot = telegram.Bot(token = '781220926:AAG-B9JwIQlrfzyoGUYtJiM1hZWAArvh1JA')
# for i in bot.getUpdates():
#     print(i.message)

# print(bot.get_me())
bot.sendMessage(chat_id = 848365857, text="테스트입니다.")