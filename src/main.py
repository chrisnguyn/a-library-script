from selenium import webdriver
import os
import time as t

username = (open("username.txt", "r")).read()
password = (open("password.txt", "r")).read()
room_index = { "a" : 2, "b" : 3, "c" : 2, "d" : 3, "e" : 4 }
room_length = { "30min" : 1, "1hr" : 2, "1hr30" : 3, "2hr" : 4, "2hr30" : 5, "3hr" : 6 }

month = input("Month (1 - 12): ")
if int(month) < 10:
    month = "0" + month

day = input("Day (1 - 31): ")

area = input("Library section (1 or 2): ")
if int(area) == 1:
    room = input("Room (A or B): ").lower()
else:
    room = input("Room (C, D, or E): ").lower()

time = input("Start time (1 - 30; 1 = 8:00am, 2 = 8:30am, 15 = 3:00pm, 30 = 10:30pm): ")
length = input("Length of booking (30min, 1hr, 1hr30, 2hr, 2hr30, 3hr): ")

url1 = "https://www.library.yorku.ca/rooms/steacie/day.php?year=2020&month=" + month + "&day=" + day + "&area=" + area
url2 = "//*[@id=\"day_main\"]/tbody/tr[" + time + "]/td[" + str(room_index.get(room)) + "]/div/a" # //*[@id="day_main"]/tbody/tr[15]/td[2]/div/a
url3 = "//*[@id=\"end_seconds\"]/option[" + str(room_length.get(length)) + "]" # //*[@id="end_seconds"]/option[6]

driver = webdriver.Chrome() # open chrome
driver.get(url1) # navigate to website

t.sleep(5) # give page time to load otherwise error

driver.find_element_by_xpath(url2).click() # find the starting time and click on it
driver.find_element_by_xpath('//*[@id="mli"]').send_keys(username)        
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)       
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input').click() # login after putting credentials

t.sleep(5) # give page time to load again

driver.find_element_by_xpath('//*[@id="name"]').send_keys("Hardcore study session") # default booking title
driver.find_element_by_xpath('//*[@id="description"]').send_keys("We studying very hard") # default booking description
driver.find_element_by_xpath(url3).click()
driver.find_element_by_xpath('//*[@id="edit_entry_submit_save"]/input').click()

# NOTES!
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
# //*[@id="end_seconds"]/option[6] - 3 hours
# //*[@id="end_seconds"]/option[1] - 30min