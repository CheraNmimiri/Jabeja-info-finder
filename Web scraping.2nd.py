from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.common.by import By
import arabic_reshaper
from selenium.webdriver.support.wait import WebDriverWait

from bidi.algorithm import get_display
import time
item_key = []
item_value = []
info = {}
key1_xpatch = ["""//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[1]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[2]/h4""",
               """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[3]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[4]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[5]/h4"""]
key2_xpatch = ["""//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[1]/h4""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[2]/h4""",
               """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[3]/h4""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[4]/h4""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[5]/h4"""]

value1_xpatch = ["""//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[1]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[2]/div/span""",
                """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[3]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[4]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[5]/div/span"""]
value2_xpatch =["""//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[1]/div/span""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[2]/div/span""",
                """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[3]/div/span""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[4]/div/span""", """//*[@id="singleJob"]/div[1]/div/div[1]/section/ul[1]/li[5]/div/span"""]


def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted


driver = webdriver.Chrome(
    executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://jobinja.ir/")
driver.maximize_window()
sign_in = driver.find_element(
    By.XPATH, """//*[@id="home2"]/div/header/div[1]/div/div[2]/div[2]/div[1]/a[1]""")
sign_in.click()
email_bar = driver.find_element(By.XPATH, """//*[@id="identifier"]""")
email_bar.send_keys("rename@gmail.com")
pass_bar = driver.find_element(By.XPATH, """//*[@id="password"]""")
pass_bar.send_keys("12345678")
sign = driver.find_element(
    By.XPATH, """//*[@id="sign-in"]/div/div/div[1]/form/div[2]/div/input[4]""")
sign.click()
driver.implicitly_wait(15)
search = driver.find_element(
    By.XPATH, """//*[@id="home2"]/div/div[2]/div/form/div[4]/button""")
search.click()
driver.implicitly_wait(15)
for p in range(1, 18):
    page = driver.get(
        f"https://jobinja.ir/jobs?&b=&filters%5Bjob_categories%5D%5B0%5D=&filters%5Bkeywords%5D%5B0%5D=.net&filters%5Blocations%5D%5B0%5D=&page={p}")
    driver.implicitly_wait(10)
    for i in range(1, 21):
        if p == 4 and i == 7:
            continue
        if p == 10 and i == 15:
            continue
        if p == 13 and i == 18:
            continue
        if p == 17 and i == 2:
            break
        title = driver.find_element(
            By.XPATH, f"""//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul/li[{i}]/div/div[1]/h2/a""")
        title.click()
        driver.switch_to.window(driver.window_handles[1])
        for k in key1_xpatch or key2_xpatch:
            a = driver.find_element(By.XPATH, k)
            item_key.append(convert(a.text))
       
        for q in value1_xpatch or value2_xpatch:
            a = driver.find_element(By.XPATH, q)
            item_value.append(convert(a.text))
        
        for m in range(len(item_value)):
            info.update({item_key[m]: item_value[m]})
        print(info)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

