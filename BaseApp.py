from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_title(self):
        return self.driver.title

    def get_attr(self,element,attr):
        return element.get_attribute(attr)

    def window_handles(self):
        return self.driver.window_handles

    def get_current_handle(self):
        return self.driver.current_window_handle

    def switch_to_page(self,handle):
        self.driver.switch_to.window(handle)
