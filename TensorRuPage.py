from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TensorRuLocators:
    LOCATOR_TENSOR_PAGE_UNITS = (By.CLASS_NAME, "tensor_ru-Index__card-title")
    LOCATOR_TENSOR_PAGE_UNIT_LINK = (By.XPATH, "//a[contains(@class, 'tensor_ru-link') and contains(@href,'about')]")
    LOCATOR_TENSOR_UNIT_PICS = (By.CLASS_NAME, "tensor_ru-About__block3-image")

class TensorRuHelper(BasePage):

    def get_url(self):
        return self.get_current_url()

    def check_unit_exists(self, unit_name):
        page_units = self.find_elements(TensorRuLocators.LOCATOR_TENSOR_PAGE_UNITS,20)
        for unit in page_units:
            if unit.text == unit_name:
                return unit
        return None

    def unit_details_link_click(self):
        unit_link = self.find_element(TensorRuLocators.LOCATOR_TENSOR_PAGE_UNIT_LINK,20).click()
        pass

    def check_pics_size_is_equal(self):
        pics = self.find_elements(TensorRuLocators.LOCATOR_TENSOR_UNIT_PICS)
        size_list = [x.get_attribute("width") + "x" + x.get_attribute("height") for x in pics]
        size_set = set(size_list)
        if len(size_set) != 1:
            return False
        return True
