from selenium import webdriver
import os
import time

class Bot:

    def __init__(self, username, password): # called when a new instance of a class is made
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.login()
    
    def login(self):
        # Subject to change. Mainly just the month, day, and area field.
        # Area=1 is rooms A and B
        # Area=2 is rooms C, D, and E
        month = input("Month: ")
        if int(month) < 10:
            month = "0" + month
        day = input("Day: ")
        area = input("Area: ")
        url = "https://www.library.yorku.ca/rooms/steacie/day.php?year=2020&month=" + month + "&day=" + day + "&area=" + area
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="day_main"]/tbody/tr[15]/td[2]/div/a').click()
        self.driver.find_element_by_xpath('//*[@id="mli"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys("EECS4101 final project")
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys("we working real hard")z