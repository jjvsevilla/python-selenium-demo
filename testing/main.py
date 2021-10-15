from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from getpass import getuser

base_url="http://the-internet.herokuapp.com/upload"

# Use on Linux VM
# driver_str = "/home/vagrant/python-selenium-demo/testing/driver/current/chromedriver"
# driver=webdriver.Chrome(executable_path=driver_str)
driver=webdriver.Chrome(executable_path=f"/Users/{getuser()}/Git/python-selenium-demo/testing/driver/current/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(base_url)
inputFile = driver.find_element(By.ID, "file-upload")
# Use on Linux VM
# csvFile = "/home/vagrant/python-selenium-demo/testing/data/file.csv"
csvFile = f"/Users/{getuser()}/Git/python-selenium-demo/testing/data/file.csv"
inputFile.send_keys(csvFile)
sleep(3)

driver.close()