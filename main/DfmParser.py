import time
from bs4 import BeautifulSoup
from selenium import webdriver


class DfmParser:
    URL_main = "https://marketwatch.dfm.ae/"
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

    def get_main_dfm_data(self):
        try:
            self.driver.get(url=self.URL_main)
            time.sleep(10)
            with open ("dfm_data.html", "w", encoding="utf-8") as file:
                file.write(self.driver.page_source)
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

    def print_main_data(self):
        with open("dfm_data.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        part = soup.find("div", class_="status-figures")
        index = part.find("span", class_="change-value market increase index").text
        percent = part.find("span", class_="changepercentage").text

        # print(index, percent)
        return index, percent
