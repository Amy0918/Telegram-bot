import requests
from bs4 import BeautifulSoup

while True:
    data = []
    stock = input()
    url = 'https://tw.stock.yahoo.com/q/q?s='+ stock    #取得公司名稱
    res = requests.get(url)
    soap = BeautifulSoup(res.text,'html.parser')
    companyName = soap.find(href="/q/bc?s="+stock)
    data.append(companyName.get_text())

    url2 = 'https://finance.yahoo.com/quote/'+ stock +'.TW/' #取得股價時間
    res2 = requests.get(url2)
    soap2 = BeautifulSoup(res2.text,'html.parser')
    time = soap2.find(id="quote-market-notice")
    data.append(time.get_text())

    url3 = 'https://finance.yahoo.com/quote/'+ stock +'.TW/'  #取得股價
    res3 = requests.get(url3)
    soap3 = BeautifulSoup(res3.text,'html.parser')
    price = soap3.find(class_="Trsdu(0.3s)")
    data.append(price.get_text())

    print(data)

#未做如果沒有擷取到資料print(NONE)
