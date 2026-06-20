from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FlightResultsPage(BasePage):
    HEADING = (By.TAG_NAME, "h3")
    FLIGHT_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    CHOOSE_BTNS = (By.CSS_SELECTOR, "input[type='submit']")

    def get_heading(self):
        return self.get_text(*self.HEADING)

    def get_flight_count(self):
        return len(self.find_all(*self.FLIGHT_ROWS))

    def get_flight_details(self):
        rows = self.find_all(*self.FLIGHT_ROWS)
        flights = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            flights.append({
                "airline": cols[2].text,
                "price": float(cols[5].text.replace("$", "")),
            })
        return flights

    def get_prices(self):
        return [f["price"] for f in self.get_flight_details()]

    def choose_flight(self, index=0):
        xpath = (By.XPATH, f"//table/tbody/tr[{index + 1}]//input[@type='submit']")
        self.click(*xpath)
