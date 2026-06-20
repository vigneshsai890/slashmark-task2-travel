import pytest
from pages.travel.search_page import FlightSearchPage
from pages.travel.results_page import FlightResultsPage


@pytest.mark.travel
class TestFlightSearch:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.search = FlightSearchPage(driver).open()

    def test_page_loads(self, driver):
        assert "BlazeDemo" in driver.title

    def test_departure_dropdown_has_options(self, driver):
        options = self.search.get_departure_options()
        assert len(options) > 0

    def test_destination_dropdown_has_options(self, driver):
        options = self.search.get_destination_options()
        assert len(options) > 0

    @pytest.mark.parametrize("departure,destination", [
        ("Paris", "Buenos Aires"),
        ("Philadelphia", "Rome"),
        ("Boston", "London"),
        ("Portland", "Berlin"),
        ("San Diego", "Dublin"),
        ("Mexico City", "Cairo"),
    ])
    def test_search_various_routes(self, driver, departure, destination):
        self.search.select_departure(departure)
        self.search.select_destination(destination)
        self.search.search_flights()
        results = FlightResultsPage(driver)
        assert results.get_flight_count() > 0

    @pytest.mark.smoke
    def test_search_returns_flights(self, driver):
        self.search.select_departure("Paris")
        self.search.select_destination("Buenos Aires")
        self.search.search_flights()
        results = FlightResultsPage(driver)
        heading = results.get_heading()
        assert "Paris" in heading and "Buenos Aires" in heading
