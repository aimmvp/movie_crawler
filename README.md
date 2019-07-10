## 파이썬으로 영화 예매 오픈 알리미 만들기

### inflearn 강의
[파이썬으로 영화 예매 오픈 알리미 만들기](https://www.inflearn.com/course/영화예매-파이썬#)
  - Python
    * BeautifulSoup
    * Telegram
  - Telegram Bot
  - AWS EC2

### aws key file 권한 설정
```
chmod 600 key_file.pem
```

### aws ubuntu 기본 세팅
```
sudo apt-get update
sudo apt install python3-pip
pip3 install requests bs4 python3-telegram-bot apscheduler
```


nohup python3 movie_crawler.py &