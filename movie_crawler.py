import requests
from bs4 import BeautifulSoup
import telegram

myId = 848365857
bot = telegram.Bot(token = '781220926:AAG-B9JwIQlrfzyoGUYtJiM1hZWAArvh1JA')
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190709"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')
telegram_message = "";
if(imax):
    imax = imax.find_parent('div', class_ = 'col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    telegram_message = title + ' IMAX 예매가 열렸습니다.'

else: 
    telegram_message = title + ' IMAX 예매가 아직 열리지 않았습니다.'

bot.sendMessage(chat_id =myId, text= telegram_message)     
