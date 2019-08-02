from selenium.webdriver.common.by import By

from pages.home_page import GoogleHomePage


class GoogleResultsPage:
    LINK_DIVS = (By.XPATH, '//div[@class="g"]')

    def __init__(self, browser):
        self.browser = browser

    def link_divs_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def search_input_value(self):
        search_input = self.browser.find_element(*GoogleHomePage.SEARCH_INPUT)
        return search_input.get_attribute('value')
