from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    CONFIRMATION_ID = (By.CSS_SELECTOR, "table tbody tr:nth-child(1) td:nth-child(2)")

    def get_heading(self):
        return self.get_text(*self.HEADING)

    def get_confirmation_details(self):
        rows = self.find_all(*self.TABLE_ROWS)
        details = {}
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 2:
                details[cols[0].text.strip()] = cols[1].text.strip()
        return details

    def is_booking_confirmed(self):
        return "Thank you" in self.get_heading()
