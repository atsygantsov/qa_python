# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def go_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def go_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def add_new_group(self, wd, g_name, g_header, g_footer):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(g_name)
        wd.find_element_by_css_selector("#content > form").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(g_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(g_footer)
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def click_on_home(self, wd):
        wd.find_element_by_link_text("home").click()

    def test_add_group(self):
        wd = self.wd
        self.go_home_page(wd)
        self.login(wd, username = "admin",password = "secret")
        self.go_to_groups_page(wd)
        self.add_new_group(wd, g_name="test", g_header="test", g_footer="foot")
        self.go_to_groups_page(wd)
        self.click_on_home(wd)
        self.logout(wd)


    def test_add_empty_group(self):
        wd = self.wd
        self.go_home_page(wd)
        self.login(wd, username = "admin",password = "secret")
        self.go_to_groups_page(wd)
        self.add_new_group(wd, g_name="", g_header="", g_footer="")
        self.go_to_groups_page(wd)
        self.click_on_home(wd)
        self.logout(wd)

    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
