from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

Browser_URL = driver.get("https://allocationenginedev.service-now.com/ae")

driver.maximize_window()
driver.implicitly_wait(40)

driver.find_element(By.XPATH, "//input[@id='username']").send_keys("sai.subramaniam")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Iopex@2023")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


Expected_URL = "https://allocationenginedev.service-now.com/ae"
# Actual_URL = "https://allocationenginedev.service-now.com/ae"

if Expected_URL == driver.current_url:
    print("Test passed")
else:
    print("Test Failed")

driver.quit()