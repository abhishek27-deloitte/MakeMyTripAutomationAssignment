# makemyTrip
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("https://www.makemytrip.com/")
        self.driver.find_element(By.CLASS_NAME, "commonModal__close").click()

        # act_title = self.driver.title
        #
        # if act_title == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday":
        #     assert True
        #     self.driver.implicitly_wait(5)
        #     self.driver.close()
        #     print("********Home-Page title test is passed*********")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage-title.png")
        #     self.driver.close()
        #     print("********Home-Page title test is failed*********")
        #     assert False


    def select_flight_option(self):
        self.driver.find_element(By.XPATH, "//span[text()='Flights']").click()

    def enter_departure_city(self, city):
        self.driver.find_element(By.ID, "fromCity").send_keys(city)

    def enter_destination_city(self, city):
        self.driver.find_element(By.ID, "toCity").send_keys(city) #//*[@id="react-autowhatever-1-section-0-item-0"]/div/div/p[1]/span[1]/span
        self.driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']/div/div/p[1]/span[1]/span").click()
        self.driver.implicitly_wait(20)

    def select_departure_date(self, date):
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{date}']").click()

    def click_search(self):
        self.driver.find_element(By.XPATH, "//a[text()='Search']").click()
        self.driver.implicitly_wait(20)
