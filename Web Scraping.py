from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.common.by import By
import arabic_reshaper
from bidi.algorithm import get_display
import time


def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted
item_key = []
item_value = []
info = {}

driver = webdriver.Edge(
    executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")

job_request_url = "https://jobinja.ir/companies/noavaran-pardazesh-gostar-nasr/jobs/Csgh/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3-%D8%AA%D8%B3%D8%AA-%D9%86%D8%B1%D9%85-%D8%A7%D9%81%D8%B2%D8%A7%D8%B1-%D8%AE%D8%A7%D9%86%D9%85-%D8%AF%D8%B1-%D9%86%D9%88%D8%A2%D9%88%D8%B1%D8%A7%D9%86-%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2%D8%B4-%DA%AF%D8%B3%D8%AA%D8%B1-%D9%86%D8%B5%D8%B1?_ref=16"
driver.get(job_request_url)
driver.implicitly_wait(5)
key_xpatch = ["""//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[1]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[2]/h4""",
              """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[3]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[4]/h4""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[5]/h4"""]
value_xpatch = ["""//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[1]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[2]/div/span""",
                """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[3]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[4]/div/span""", """//*[@id="singleJob"]/div/div/div[1]/section/ul[1]/li[5]/div/span"""]

for i in key_xpatch:
    a = driver.find_element(By.XPATH, i)
    item_key.append(convert(a.text))
for i in value_xpatch:
    a = driver.find_element(By.XPATH, i)
    item_value.append(convert(a.text))
for i in range(len(item_value)):
    info.update({item_key[i]: item_value[i]})
print(info)

