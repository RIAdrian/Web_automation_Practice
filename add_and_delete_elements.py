from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configure the Service for ChromeDriver
service = Service("C:\\Users\\rente\\Downloads\\chromedriver-win64\\chromedriver.exe")

# Function to start a new WebDriver instance
def start_driver():
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    return driver

# Function to add elements
def add_elements(driver, number):
    for _ in range(number):
        driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

# Function to delete all elements
def delete_elements(driver):
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    for button in delete_buttons:
        button.click()

try:
    # 1. Test: User can create and delete a single element
    print("Test 1: Adding and deleting a single element.")
    driver = start_driver()  # Start a new driver for Test 1
    add_elements(driver, 1)  # Add one element
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 1, "Element was not added."
    print("One element added successfully.")
    delete_elements(driver)  # Delete the element
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 0, "Element was not deleted."
    print("One element deleted successfully.\n")
    driver.quit()  # Close the browser

    # 2. Test: User can create 10 elements
    print("Test 2: Adding 10 elements.")
    driver = start_driver()  # Start a new driver for Test 2
    add_elements(driver, 10)  # Add 10 elements
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 10, "Not all 10 elements were added."
    print("10 elements added successfully.\n")
    driver.quit()  # Close the browser

    # 3. Test: User can create and delete 10 elements
    print("Test 3: Adding and deleting 10 elements.")
    driver = start_driver()  # Start a new driver for Test 3
    add_elements(driver, 10)  # Add 10 elements
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 10, "Not all 10 elements were added."
    print("10 elements added successfully.")
    delete_elements(driver)  # Delete all elements
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 0, "Not all 10 elements were deleted."
    print("10 elements deleted successfully.\n")
    driver.quit()  # Close the browser

    # 4. Test: User can add 50 elements, then delete 25, and verify the remaining count
    print("Test 4: Adding 50 elements, deleting 25, and verifying the remaining count.")
    driver = start_driver()  # Start a new driver for Test 4
    add_elements(driver, 50)  # Add 50 elements
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 50, "Not all 50 elements were added."
    print("50 elements added successfully.")
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")[:25]  # Select the first 25 buttons
    for button in delete_buttons:
        button.click()  # Delete 25 elements
    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 25, "The remaining element count is incorrect."
    print("25 elements deleted successfully. 25 elements remain.\n")
    driver.quit()  # Close the browser

except Exception as e:
    print(f"Error encountered during testing: {e}")
