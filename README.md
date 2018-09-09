# Python Bot


## 청와대 청원 
청원 추천순 1,2,3 페이지를 저장합니다

## 인터파크 포인트
포인트를 읽어서 텔레그램으로 전송합니다
인터파크 아이디/패스워드
텔레그램 봇토큰/받을유저ID 필요

pip install python-telegram-bot --upgrade

## 환경구성

### 공통

셀레니움 필요
```
pip install selenium
```

### 리눅스

크롬드라이버 필요
```bash
sudo apt-get install chromium-browser
sudo apt-get install chromium-chromedriver
```



## 라즈베리파이
python3.6 수동설치 필요합니다 (2018-09-08 기준 raspbian 최신 3.5.3)

```bash
sudo apt-get update
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz
cd Python-3.6.5
./configure
make -j 4
sudo make altinstall
```

pip3.6 사용
```bash
sudo apt-get install libffi-dev,python-cffi
sudo pip3.6 install --upgrade pip
sudo pip3.6 install selenium
sudo pip3.6 install python-telegram-bot --upgrade
```
crontab 에서는 패스지정 필요함
```
PATH=/usr/local/bin:/usr/bin:$PATH
PYTHONPATH=/usr/local/lib/python3.6/site-packages
````
