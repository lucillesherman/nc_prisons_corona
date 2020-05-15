from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
browser = webdriver.Chrome(executable_path = "/Users/user/Desktop/nopolitics/coronavirus_counts/chromedriver 2", chrome_options=option)
browser.get("https://opus.doc.state.nc.us/DOPCovid19Stats/services/facilitystatsServlet")

# element = browser.find_element_by_xpath('//*[@id="node-10909"]/div/div/div/div/div[1]/section/section/div[2]/div/div/div')

# actions = ActionChains(browser)

# browser.execute_script("arguments[0].scrollIntoView();", element)

results = browser.page_source
soup = BeautifulSoup(results, "html.parser")
table = soup.find("table")
output = ""
count = 1

for headers in soup.find_all('th'):
	output += '"' + headers.text.strip() + '"' + ","
output += "\n"
for t in soup.find_all('td'):
	output += '"' + t.text.strip() + '"' + ","
	count = count + 1
	if count == 5:
		output += "\n"
		count = 1

import datetime
current_date = datetime.datetime.now()
filename = "prisonactionscovid"+str(current_date.strftime("%Y-%m-%d %H:%M"))

with open(filename + ".csv", "w") as csv_file:
	csv_file.write(str(output))
	csv_file.close()
browser.close()
browser.quit()