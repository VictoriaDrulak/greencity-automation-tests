from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventsPage:

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    SEARCH_INPUT = (By.CSS_SELECTOR, "input")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def search_event(self, text):
        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search.clear()
        search.send_keys(text)

    def get_search_value(self):
        search = self.driver.find_element(*self.SEARCH_INPUT)
        return search.get_attribute("value")