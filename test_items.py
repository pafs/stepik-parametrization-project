from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

class TestRun:
    def test_btn_add_to_basket_is_visible(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        assert ec.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), \
            "Add to basket button is not visible"
