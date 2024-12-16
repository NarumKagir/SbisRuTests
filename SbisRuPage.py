from itertools import count
from operator import contains

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisRuLocators:
    LOCATOR_SBIS_CONTACTS_TAB = (By.CLASS_NAME, "sbisru-Header-ContactsMenu")
    LOCATOR_SBIS_CONTACTS_POPUP_LINK = (By.XPATH, "//a[contains(@href,'contacts') and contains(@class,'sbisru-link')]")
    LOCATOR_SBIS_REGION_NAME = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    LOCATOR_SBIS_REGION_LINK = (By.CLASS_NAME, "sbis_ru-Region-Chooser")
    LOCATOR_SBIS_REGION_LIST = (By.XPATH,"//li/span[contains(@class,'sbis_ru-link')]")
    LOCATOR_SBIS_CONTACTS_LINK = (By.CLASS_NAME,"sbis_ru-Region-Chooser")
    LOCATOR_SBIS_REGION_TEXT = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    LOCATOR_SBIS_PARTNERS_LIST = (By.CLASS_NAME, "sbisru-Contacts-List__item")
    LOCATOR_SBIS_REGION_POPUP_LINK = (By.CLASS_NAME, "sbis_ru-Region-Chooser")
    LOCATOR_SBIS_CONTACTS_LOGO_TENSOR = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")

class SbisRuHelper(BasePage):

    def contacts_tab_click(self):
        self.find_element(SbisRuLocators.LOCATOR_SBIS_CONTACTS_TAB).click()

    def contacts_link_click(self):
        self.find_element(SbisRuLocators.LOCATOR_SBIS_CONTACTS_POPUP_LINK).click()

    def check_region_name(self):
        search_field = self.find_element(SbisRuLocators.LOCATOR_SBIS_REGION_NAME,20).text
        return search_field

    def click_on_region_panel_link(self,region_name):
        regions_list = self.find_elements(SbisRuLocators.LOCATOR_SBIS_REGION_LIST,20)
        region_link = [x for x in regions_list if x.get_attribute("title") == region_name]
        region_link[0].click()

    def get_url(self):
        return self.get_current_url()

    def get_title(self):
        return self.get_current_title()

    def current_region_click(self):
        search_field = self.find_element(SbisRuLocators.LOCATOR_SBIS_REGION_TEXT)
        search_field.click()

    def check_partners_list(self):
        all_list = self.find_elements(SbisRuLocators.LOCATOR_SBIS_PARTNERS_LIST)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        if len(nav_bar_menu) == 0:
            return None
        return nav_bar_menu[0]

    def get_partners_list(self):
        return self.find_elements(SbisRuLocators.LOCATOR_SBIS_PARTNERS_LIST)

    def tensor_logo_click(self):
        search_field = self.find_element(SbisRuLocators.LOCATOR_SBIS_CONTACTS_LOGO_TENSOR)
        search_link = self.get_attr(search_field,"href")
        search_field.click()
        return search_link

    def switch_to_tensor_ru(self):
        sbisru_handle = self.get_current_handle()
        window_handles = self.window_handles()
        for window_handle in window_handles:
            if window_handle != sbisru_handle:
                self.switch_to_page(window_handle)
