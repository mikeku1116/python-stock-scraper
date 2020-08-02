# python-stock-scraper #

## 專案介紹 ##

本專案以Yahoo奇摩股市為例，利用Python網頁爬蟲取得關注的股票當日行情，並且動態的存入MySQL資料庫中，可以搭配[[Python爬蟲教學]輕鬆學會Python網頁爬蟲與MySQL資料庫的整合方式](https://www.learncodewithmike.com/2020/08/python-scraper-integrate-with-mysql.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境：

`$ pipenv shell`

最後，安裝MySQL資料庫，並且依照[[Python爬蟲教學]輕鬆學會Python網頁爬蟲與MySQL資料庫的整合方式](https://www.learncodewithmike.com/2020/08/python-scraper-integrate-with-mysql.html)部落格文章來建立相關的資料表欄位，以及在scraper.py檔案中，設定MySQL資料庫的密碼，即可執行範例程式。