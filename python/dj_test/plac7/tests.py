from django.test import TestCase
from django.test import LiveServerTestCase
from django.urls import reverse_lazy
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


class LoginTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get("https://www.yahoo.co.jp/")
        # self.selenium.get('http://localhost:8000' + str(reverse_lazy('login')))

        # # ログイン
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('username')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('password')
        # self.selenium.find_element_by_class_name('btn').click()

        # # ページタイトルの検証
        # self.assertEquals('ログイン後ページ', self.selenium.title)

