
import pytest
from POM.home_page import HomePage
from POM.search_results_page import SearchResultsPage
from POM.payment_page import PaymentPage

@pytest.mark.usefixtures("setup")
class TestMakeMyTrip:
    def test_book_flight(self):
        home_page = HomePage(self.driver)
        search_results_page = SearchResultsPage(self.driver)
        payment_page = PaymentPage(self.driver)

        home_page.go_to_home_page()
        home_page.select_flight_option()
        home_page.enter_departure_city("New Delhi")
        home_page.enter_destination_city("Mumbai")
        home_page.select_departure_date("Fri Apr 25 2025")
        home_page.click_search()

        search_results_page.select_first_flight()

        search_results_page.handle_alert()

        payment_page.proceed_to_payment()
