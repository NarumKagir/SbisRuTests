from operator import contains
from SbisRuPage import SbisRuHelper

def test_sbis_contacts(browser):
    sbisru_page = SbisRuHelper(browser)
    sbisru_page.go_to_site()
    sbisru_page.contacts_tab_click()
    sbisru_page.contacts_link_click()
    test_region_names = ["Ярославская обл.","Камчатский край"]
    #
    current_region_check = sbisru_page.check_region_name()
    if current_region_check == test_region_names[0]:
        print(f"Current region is {current_region_check}. Test passed")
    else:
        print(f"Current region is {current_region_check}. Test failed")

    current_url = sbisru_page.get_url()
    current_partners_list = sbisru_page.get_partners_list()
    sbisru_page.current_region_click()
    sbisru_page.click_on_region_panel_link(test_region_names[1])
    current_region_check = sbisru_page.check_region_name()
    if current_region_check == test_region_names[1]:
        print(f"Current region is {current_region_check}. Test passed")
    else:
        print(f"Current region is {current_region_check}. Test failed")

    new_partners_list = sbisru_page.get_partners_list()
    if new_partners_list == current_partners_list:
        print("Partners list is unchanged")
    else:
        print("Partners list changed")

    current_title = sbisru_page.get_title()
    if contains(current_title, test_region_names[1]):
        print("Title changed")
    else:
        print("Title is unchanged")

    new_url = sbisru_page.get_url()
    assert new_url != current_url, "URL didn't changed. Test failed"
