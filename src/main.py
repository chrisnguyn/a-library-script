from selenium import webdriver
import os
import time as t

username = (open("username.txt", "r")).read()
password = (open("password.txt", "r")).read()
roomindex = { "A" : 2, "B" : 3, "C" : 2, "D" : 3, "E" : 4}

month = input("Month (prefix 0 if < 10, 9 becomes 09): ")
day = input("Day: ")
area = input("Section (1-2, where 1 is AB and 2 is CDE): ")
room = input("Room (A or B (if section 1), or C, D or E (if section 2): ")
time = input("Time (1-30; 1 = 8:00am, 2 = 8:30am, 15 = 3:00pm, 30 = 10:30pm): ")
url1 = "https://www.library.yorku.ca/rooms/steacie/day.php?year=2020&month=" + month + "&day=" + day + "&area=" + area
url2 = "//*[@id=\"day_main\"]/tbody/tr[" + time + "]/td[" + str(roomindex.get(room)) + "]/div/a" # //*[@id="day_main"]/tbody/tr[15]/td[2]/div/a
driver = webdriver.Chrome()
driver.get(url1)

t.sleep(5)

driver.find_element_by_xpath(url2).click()
driver.find_element_by_xpath('//*[@id="mli"]').send_keys(username)        
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)       
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input').click() # LOGIN

t.sleep(5)

driver.find_element_by_xpath('//*[@id="name"]').send_keys("Hardcore study session")
driver.find_element_by_xpath('//*[@id="description"]').send_keys("We studying very hard")
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
# //*[@id="end_seconds"]/option[6]