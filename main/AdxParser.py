import time
import json
import csv
from bs4 import BeautifulSoup
from selenium import webdriver


class AdxParser:
    URL_main = "https://www.adx.ae/english/Pages/marketwatch.aspx?isdlg=1"
    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/106.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        executable_path="C:\\FolderForGitHub\\TradesCollector\\main\\chromedriver.exe",
        options=options
    )

    def __init__(self):
        self.info = []

    def get_main_adx_data(self):
        try:
            self.driver.get(url=self.URL_main)
            time.sleep(32)
            with open("adx_data.html", "w", encoding="utf-8") as file:
                file.write(self.driver.page_source)
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

    # def collect_all_adx_data(self):
    #     with open("adx_data.html") as file:
    #         src = file.read()
    #
    #     soup = BeautifulSoup(src, "lxml")
    #     table = soup.find("table", class_="display dataTable no-footer")
    #     data_odd = table.findAll("tr", class_="odd")
    #     data_even = table.findAll("tr", class_="even")
    #
    #     print(table)
    #     # with open("all_data.json", "a", encoding="utf-8") as file:
    #     #     json.dump(data_odd, file, indent=4, ensure_ascii=False)
    #     #     json.dump(data_even, file, indent=4, ensure_ascii=False)

    def print_main_data(self):
        with open("adx_data.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        index = soup.find("span", class_="part1").text
        percent = soup.find("span", class_="part3").text

        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(
                [index, percent]
            )

        # print(index, percent)
        return index, percent
