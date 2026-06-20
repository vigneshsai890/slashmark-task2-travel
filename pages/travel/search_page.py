from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class FlightSearchPage(BasePage):
    URL = "https://blazedemo.com"

    DEPART_CITY = (By.NAME, "fromPort")
    DEST_CITY = (By.NAME, "toPort")
    FIND_FLIGHTS_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def select_departure(self, city):
        Select(self.find(*self.DEPART_CITY)).select_by_visible_text(city)
        return self

    def select_destination(self, city):
        Select(self.find(*self.DEST_CITY)).select_by_visible_text(city)
        return self

    def get_departure_options(self):
        select = Select(self.find(*self.DEPART_CITY))
        return [o.text for o in select.options]

    def get_destination_options(self):
        select = Select(self.find(*self.DEST_CITY))
        return [o.text for o in select.options]

    def search_flights(self):
        self.click(*self.FIND_FLIGHTS_BTN)
