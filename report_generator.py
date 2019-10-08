from selenium import webdriver
import os
import time

browser = webdriver.Chrome("/usr/bin/chromedriver") 
browser.maximize_window() 

#URL for eLab
browser.get('http://care.srmist.edu.in/ktroops/') 

#Your username and password
username = "usrname"
password = "pswrd"
  
usr = browser.find_element_by_name('username')
usr.send_keys(username)

pwd = browser.find_element_by_name('password')
pwd.send_keys(password)

browser.find_elements_by_class_name('mat-button-wrapper')[1].click()

time.sleep(5)

browser.find_element_by_class_name('courseName').click()

#set the URL for the question you want to start with
browser.get('http://care.srmist.edu.in/ktroops/student/solve/2420115')

time.sleep(3)

"""
!!!! BUGS !!!!
->Gets stuck if encounters an unsuccessful evaluation 
->Gets stuck if encounters a problem with single test case

!!! WARNINGS !!!
->Change the sleep time according to the internet speed

"""

for x in range(100):

    browser.find_elements_by_class_name("mat-button-wrapper")[9].click()
    time.sleep(2)
    path, dirs, files = next(os.walk("/home/artistbanda/Downloads"))
    file_count_1 = file_count_2 = len(files)
    while (file_count_1 == file_count_2):
        browser.find_element_by_link_text("file_download").click()
        time.sleep(2)
        #  Set the default download path for chrome
        path, dirs, files = next(os.walk("/home/artistbanda/Downloads"))
        file_count_2 = len(files)
    browser.find_elements_by_class_name("mat-button-wrapper")[4].click()
    time.sleep(2)
    print(x + 1)