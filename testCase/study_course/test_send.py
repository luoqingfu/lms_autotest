#coding=utf-8
import unittest

from time import sleep

from selenium import webdriver




class test_web_demo(unittest.TestCase):
    def test_baidu(self):
        driver = webdriver.Chrome('/Users/qfl/lqf_work/selenium_work/lms_autotest/driver/chromedriver')
        driver.maximize_window()
        driver.get("https://4xjhtu.beta.e-ducation.cn/live/1413/login")
        el1 = driver.find_element_by_css_selector('#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(2) > input')
        el1.send_keys('13226349780')
        el2 = driver.find_element_by_css_selector('#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(3) > input')
        el2.send_keys('000001')
        el3 = driver.find_element_by_css_selector('#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(4) > button')
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_id('mywords')
        el4.send_keys('12123213')
        sleep(0.2)
        el5 = driver.find_element_by_id('jssend')
        el5.click()
