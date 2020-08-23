# python-stock-scraper #

## 專案介紹 ##

本專案以Yahoo奇摩股市為例，開發Python網頁爬蟲取得關注的股票當日行情，並且提供了四個方法(Method)，
包含：
* scrape()
* save()
* export()
* gsheet()
其中，scrape()方法(Method)為爬取關注的股票當日行情資料，而save()方法(Method)提供存入MySQL資料庫的功能，可以搭配[[Python爬蟲教學]輕鬆學會Python網頁爬蟲與MySQL資料庫的整合方式](https://www.learncodewithmike.com/2020/08/python-scraper-integrate-with-mysql.html)部落格文章來進行學習。

另外，export()方法(Method)整合openpyxl套件，提供將Python網頁爬蟲所取得的股票當日行情資料，匯出成Excel檔案，並且在其中的漲跌欄位，客製化顯示儲存格的文字顏色，可以搭配[[Python爬蟲教學]活用openpyxl套件將爬取的資料寫入Excel檔案](https://www.learncodewithmike.com/2020/08/python-write-to-an-excel-file-using-openpyxl-module.html)部落格文章來進行學習。

最後，gsheet()方法(Method)則是透過Google Sheet API，將Python網頁爬蟲取得的股票當日行情資料，寫入雲端Google Sheet試算表中，可以搭配[[Python爬蟲教學]解析如何串接Google Sheet試算表寫入爬取的資料](https://www.learncodewithmike.com/2020/08/python-write-to-google-sheet.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境：

`$ pipenv shell`