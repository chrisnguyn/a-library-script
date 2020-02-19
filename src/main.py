from selenium import webdriver
import os
import time

username = (open("username.txt", "r")).read()
password = (open("password.txt", "r")).read()
driver = webdriver.Chrome()

month = input("Month: ")
if int(month) < 10:
    month = "0" + month
day = input("Day: ")
area = input("Area: ")
# time = input("Time (1-30; 1 = 8:00am, 2 = 8:30am, 15 = 3:00pm, 30 = 10:30pm): ")
url = "https://www.library.yorku.ca/rooms/steacie/day.php?year=2020&month=" + month + "&day=" + day + "&area=" + area

driver.get(url)
driver.find_element_by_xpath('//*[@id="day_main"]/tbody/tr[15]/td[2]/div/a').click() # on the library page, click the section
driver.find_element_by_xpath('//*[@id="mli"]').send_keys(username)                   # send user
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)              # send pass
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@id="name"]').send_keys("Amazon Summit Conference II")
driver.find_element_by_xpath('//*[@id="description"]').send_keys("We work at Amazon, yes")
driver.find_element_by_xpath('//*[@id="end_seconds"]/option[6]').click()
driver.find_element_by_xpath('//*[@id="edit_entry_submit_save"]/input').click()

# area=1
# 8:00am //*[@id="day_main"]/tbody/tr[1]/td[2]/div/a - room A
# 8:00am //*[@id="day_main"]/tbody/tr[1]/td[3]/div/a - room B
# area=2
# 8:00am //*[@id="day_main"]/tbody/tr[1]/td[2]/div/a - room C
# 8:00am //*[@id="day_main"]/tbody/tr[1]/td[3]/div/a - room D
# 8:00am //*[@id="day_main"]/tbody/tr[1]/td[4]/div/a - room E
# Max val: 10:30pm //*[@id="day_main"]/tbody/tr[30]/td[3]/div/a

# xpath 1 hr (default) //*[@id="end_seconds"]
# xpath 3 hr //*[@id="end_seconds"]
# //*[@id="end_seconds"]/option[6] ?