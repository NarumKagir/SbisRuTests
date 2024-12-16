from SbisRuPage import SbisRuHelper
from TensorRuPage import TensorRuHelper

def test_tensor_about_pics(browser):

    sbisru_page = SbisRuHelper(browser)
    sbisru_page.go_to_site()
    sbisru_page.contacts_tab_click()
    sbisru_page.contacts_link_click()
    sbisru_page.tensor_logo_click()
    sbisru_page.switch_to_tensor_ru()

    tensor_ru_page = TensorRuHelper(browser)
    tensor_ru_page.unit_details_link_click()
    assert tensor_ru_page.check_pics_size_is_equal(), "Pics size is not equal. Test failed."

