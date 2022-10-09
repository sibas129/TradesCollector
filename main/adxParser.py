import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import json

class adxPareser():
    URL_main = "https://www.adx.ae/english/Pages/marketwatch.aspx?isdlg=1"

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
  }

    #def __init__(self)

    def get_main_adx_data(self):
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(
        #     executable_path="C:/Users/vlad_/TradesCollector/main/chromedriver.exe",
        #     options=options)
        # try:
        #     driver.get(url=self.URL_main)
        #     sleep(5)
        #
        #     with open("index_selenium.html", "w") as file:
        #         file.write(driver.page_source)
        #
        # except Exception as ex:
        #     print(ex)
        # finally:
        #     driver.close()
        #     driver.quit()
        #
        # with open("index_selenium.html") as file:
        #     src = file.read()
        #
        # # get hotels urls
        # soup = BeautifulSoup(src, "lxml")
        #
        # # hotels_cards = soup.find_all("div", class_="hotel_card_dv")
        # #
        # # for hotel_url in hotels_cards:
        # #     hotel_url = "https://www.tury.ru" + hotel_url.find("a").get("href")
        # #     print(hotel_url)
        response = requests.get(self.URL_main, headers=self.headers)
        #
        raw_info = BeautifulSoup(response.text, "lxml")
        data = raw_info.find("div", class_="dataTables_scrollBody")
        #price = data.find("span", class_="part1").text

        return data

