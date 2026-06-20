from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookingPage(BasePage):
    NAME = (By.ID, "inputName")
    ADDRESS = (By.ID, "address")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    ZIP_CODE = (By.ID, "zipCode")
    CARD_TYPE = (By.ID, "cardType")
    CARD_NUMBER = (By.ID, "creditCardNumber")
    CARD_MONTH = (By.ID, "creditCardMonth")
    CARD_YEAR = (By.ID, "creditCardYear")
    NAME_ON_CARD = (By.ID, "nameOnCard")
    REMEMBER_ME = (By.ID, "rememberMe")
    PURCHASE_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    TOTAL_COST = (By.CSS_SELECTOR, "p:nth-of-type(3)")
    AIRLINE_INFO = (By.CSS_SELECTOR, "p:nth-of-type(2)")

    def fill_passenger_info(self, name="John Doe", address="123 Main St",
                            city="Anytown", state="CA", zip_code="12345"):
        self.type_text(*self.NAME, name)
        self.type_text(*self.ADDRESS, address)
        self.type_text(*self.CITY, city)
        self.type_text(*self.STATE, state)
        self.type_text(*self.ZIP_CODE, zip_code)
        return self

    def fill_payment_info(self, card_number="1234567890",
                          month="11", year="2027", name_on_card="John Doe"):
        self.type_text(*self.CARD_NUMBER, card_number)
        self.type_text(*self.CARD_MONTH, month)
        self.type_text(*self.CARD_YEAR, year)
        self.type_text(*self.NAME_ON_CARD, name_on_card)
        return self

    def get_displayed_price(self):
        text = self.get_text(*self.TOTAL_COST)
        return text

    def purchase(self):
        self.click(*self.PURCHASE_BTN)
