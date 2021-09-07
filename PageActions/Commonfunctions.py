"""
In this we can define a function acording to the test in a class
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class Test:

    def __init__(self):
        """

        """
        self.browser = webdriver.Chrome(r"C:\Users\Lucky\project1\Appdrives\chromedriver.exe")

    def open_browser(self, url):
        """

        :param url:
        :return:
        """
        self.browser.get(url)

    def maximize(self):
        """

        :return:
        """
        self.browser.maximize_window()

    def page_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs(self, x_path):
        """

        :param x_path:
        :return:
        """
        self.browser.find_element_by_xpath(x_path).click()

    def switch_to_frame(self, x_path):
        """

        :param x_path:
        :return:
        """
        try:
            self.browser.switch_to_frame(self.browser.find_element_by_xpath(x_path))
        except NoSuchElementException:
            raise Exception('No such Element')

    def switch(self):
        """

        :return:
        """
        self.browser.switch_to_default_content()

    def move_element(self, x_path, x_offset, y_offset):
        """

        :param x_path:
        :param x_offset:
        :param y_offset:
        :return:
        """
        time.sleep(5)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(x_path).move_by_offset(x_offset, y_offset).release().perform()

    def scrolldown(self):
        """

        :return:
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()

    def scrollup(self):
        """

        :return:
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()

    def select(self, x_path):
        """

        :param x_path:
        :return:
        """
        self.browser.find_element(By.XPATH, x_path).click()
