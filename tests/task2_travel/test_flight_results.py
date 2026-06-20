import pytest
from pages.travel.search_page import FlightSearchPage
from pages.travel.results_page import FlightResultsPage


@pytest.mark.travel
class TestFlightResults:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        search = FlightSearchPage(driver).open()
        search.select_departure("Paris")
        search.select_destination("Buenos Aires")
        search.search_flights()
        self.results = FlightResultsPage(driver)

    def test_results_heading_shows_route(self, driver):
        heading = self.results.get_heading()
        assert "Paris" in heading
        assert "Buenos Aires" in heading

    def test_multiple_flights_returned(self, driver):
        assert self.results.get_flight_count() >= 1

    def test_flights_have_prices(self, driver):
        prices = self.results.get_prices()
        assert all(p > 0 for p in prices)

    def test_flights_have_airlines(self, driver):
        flights = self.results.get_flight_details()
        assert all(len(f["airline"]) > 0 for f in flights)

    def test_choose_cheapest_flight(self, driver):
        prices = self.results.get_prices()
        cheapest_index = prices.index(min(prices))
        self.results.choose_flight(cheapest_index)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.url_contains("purchase"))
        assert "purchase" in driver.current_url

    def test_choose_first_flight(self, driver):
        self.results.choose_flight(0)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.url_contains("purchase"))
        assert "purchase" in driver.current_url
