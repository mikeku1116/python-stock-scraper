from bs4 import BeautifulSoup
import requests


class Stock:
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers

    def scrape(self):

        result = list()

        for stock_number in self.stock_numbers:

            response = requests.get(
                "https://tw.stock.yahoo.com/q/q?s=" + stock_number)
            soup = BeautifulSoup(response.text.replace("加到投資組合", ""), "lxml")

            stock_date = soup.find(
                "font", {"class": "tt"}).getText().strip()[-9:]

            tables = soup.find_all("table")[2]
            tds = tables.find_all("td")[0:11]

            result.append((stock_date,) +
                          tuple(td.getText().strip() for td in tds))
        return result
