import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configure the Service for ChromeDriver
service = Service("....")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)


def test_file_upload(driver_setup_teardown):
    driver = driver_setup_teardown
    filename = 'some-file.txt'
    file = os.path.join(os.getcwd(), filename)
    driver.get('https://the-internet.herokuapp.com/upload')
    driver.find_element(By.ID, 'file-upload').send_keys(file)
    driver.find_element(By.ID, 'file-submit').click()
    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, "uploaded file should be %s" % filename
    if driver.find_element(By.ID, 'uploaded-files'): print ("Test passed!")


test_file_upload(driver)
