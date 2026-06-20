import pytest
from pages.travel.search_page import FlightSearchPage
from pages.travel.results_page import FlightResultsPage
from pages.travel.booking_page import BookingPage
from pages.travel.confirmation_page import ConfirmationPage


@pytest.mark.travel
class TestBooking:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        search = FlightSearchPage(driver).open()
        search.select_departure("Paris")
        search.select_destination("Buenos Aires")
        search.search_flights()
        FlightResultsPage(driver).choose_flight(0)
        self.booking = BookingPage(driver)
        self.confirmation = ConfirmationPage(driver)

    @pytest.mark.smoke
    def test_complete_booking(self, driver):
        self.booking.fill_passenger_info()
        self.booking.fill_payment_info()
        self.booking.purchase()
        assert self.confirmation.is_booking_confirmed()

    def test_booking_page_shows_price(self, driver):
        price_text = self.booking.get_displayed_price()
        assert "$" in price_text or "Price" in price_text or "Total" in price_text

    @pytest.mark.parametrize("name,city,state", [
        ("Alice Johnson", "New York", "NY"),
        ("Bob Smith", "Los Angeles", "CA"),
        ("Carlos Garcia", "Miami", "FL"),
    ])
    def test_booking_with_different_passengers(self, driver, name, city, state):
        self.booking.fill_passenger_info(name=name, city=city, state=state)
        self.booking.fill_payment_info()
        self.booking.purchase()
        assert self.confirmation.is_booking_confirmed()

    def test_confirmation_has_id(self, driver):
        self.booking.fill_passenger_info()
        self.booking.fill_payment_info()
        self.booking.purchase()
        details = self.confirmation.get_confirmation_details()
        assert len(details) > 0

    def test_confirmation_heading(self, driver):
        self.booking.fill_passenger_info()
        self.booking.fill_payment_info()
        self.booking.purchase()
        heading = self.confirmation.get_heading()
        assert "Thank you" in heading


@pytest.mark.travel
class TestEndToEnd:
    @pytest.mark.smoke
    def test_full_journey_paris_to_buenos_aires(self, driver):
        search = FlightSearchPage(driver).open()
        search.select_departure("Paris")
        search.select_destination("Buenos Aires")
        search.search_flights()

        results = FlightResultsPage(driver)
        assert results.get_flight_count() > 0
        results.choose_flight(0)

        booking = BookingPage(driver)
        booking.fill_passenger_info(name="Vignesh Sai", city="Chennai", state="TN")
        booking.fill_payment_info(card_number="4111111111111111", month="12",
                                  year="2028", name_on_card="Vignesh Sai")
        booking.purchase()

        confirmation = ConfirmationPage(driver)
        assert confirmation.is_booking_confirmed()

    @pytest.mark.parametrize("departure,destination", [
        ("Philadelphia", "Rome"),
        ("Boston", "London"),
        ("Portland", "Berlin"),
    ])
    def test_full_journey_various_routes(self, driver, departure, destination):
        search = FlightSearchPage(driver).open()
        search.select_departure(departure)
        search.select_destination(destination)
        search.search_flights()

        results = FlightResultsPage(driver)
        results.choose_flight(0)

        booking = BookingPage(driver)
        booking.fill_passenger_info()
        booking.fill_payment_info()
        booking.purchase()

        assert ConfirmationPage(driver).is_booking_confirmed()
