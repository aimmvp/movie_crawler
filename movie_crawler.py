import requests
from bs4 import BeautifulSoup
import telegram
import mykey
from apscheduler.schedulers.blocking import BlockingScheduler


myId =  mykey.MY_ID
bot = telegram.Bot(token =  mykey.TELEGRAM_KEY)
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190709"

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    telegram_message = "";
    if(imax):
        imax = imax.find_parent('div', class_ = 'col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        telegram_message = title + ' IMAX 예매가 열렸습니다.'
        bot.sendMessage(chat_id =myId, text= telegram_message)     
        sched.pause()
    # else: 
    #     telegram_message = title + ' IMAX 예매가 아직 열리지 않았습니다.'


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()