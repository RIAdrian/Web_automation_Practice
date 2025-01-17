from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configure the Service for ChromeDriver
service = Service("C:\\Users\\rente\\Downloads\\chromedriver-win64\\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the Context Menu page
driver.get("https://the-internet.herokuapp.com/context_menu")

# Locate the context menu area
context_menu = driver.find_element(By.ID, "hot-spot")

# Perform a right-click action on the context menu area
action = ActionChains(driver)
action.context_click(context_menu).perform()

# Handle the alert that appears after right-clicking
try:
    # Wait for the alert to appear
    time.sleep(2)  # Optional: Add a wait to ensure the alert is visible
    alert = driver.switch_to.alert

    # Verify the alert message
    alert_message = alert.text
    print(f"Alert message displayed: {alert_message}")
    assert alert_message == "You selected a context menu", "Unexpected alert message!"

    # Accept the alert
    alert.accept()
    print("Alert verified and accepted successfully.")

except Exception as e:
    print(f"Error during context menu test: {e}")

finally:
    # Pause for observation (optional)
    time.sleep(2)
    # Close the browser
    driver.quit()
