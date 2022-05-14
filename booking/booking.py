import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\beher\Desktop\Coding Misc\Selenium Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR,
                                                      f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
                                                      )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR,
                                         'li[data-i="0"]'
                                         )
        first_result.click()

    def select_date(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, "xp__guests__toggle")
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                                                        'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            # if number of adults is 1, we need to get out of the while loop
            adults_value_element = self.find_element(By.ID, "group_adults")
            adults_value = adults_value_element.get_attribute('value')  # should give back adults count
            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        while count > 1:
            increase_adults_element.click()
            count -= 1

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        pass