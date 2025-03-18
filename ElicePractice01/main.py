import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

# 오늘의 집 웹 페이지 열기
driver = webdriver.Chrome(options=options)
driver.get("https://ohou.se/")
time.sleep(3)


class MainPageHeaderLoad:
    def __init__(self, driver):
        self.driver = driver

    def Main_load(self):
        try:
            header_banner = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/a')
            print("header_banner 요소 확인")
        except NoSuchElementException:
            print("header_banner 미발견")

        try:
            header_banner_close = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/button')
            print("header_banner_close 요소 확인")
        except NoSuchElementException:
            print("header_banner_close 미발견")

        try:
            header_menu = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div/div/header/div[1]/div/div/div[1]/button/span")
            print("header_menu 요소 확인")
        except NoSuchElementException:
            print("header_menu 미발견")

        try:
            header_logo = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div/div/div[2]/a")
            print("header_logo 요소 확인")
        except NoSuchElementException:
            print("header_logo 미발견")

    def house_search(self):
        try:
            search_btn = self.driver.find_element(By.XPATH, '//*[@id="global-search-combobox"]/div/input')
            search_btn.send_keys("이불")
            search_btn.send_keys(Keys.RETURN)
            time.sleep(5)
            print("검색 완료")
        except NoSuchElementException:
            print("검색창 요소를 찾을 수 없습니다.")


# 클래스 인스턴스 생성 및 실행
main_page = MainPageHeaderLoad(driver)
main_page.Main_load()
main_page.house_search()
