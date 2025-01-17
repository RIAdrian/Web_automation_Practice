from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configure the Service for ChromeDriver
service = Service("C:\\Users\\rente\\Downloads\\chromedriver-win64\\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the Checkboxes page
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Locate the checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Test scenarios
def test_checkboxes():
    try:
        # 1. Are all checkboxes unchecked initially?
        print("Test 1: Are all checkboxes unchecked?")
        all_unchecked = all(not checkbox.is_selected() for checkbox in checkboxes)
        if all_unchecked:
            print("All checkboxes are initially unchecked.\n")
        else:
            print("Not all checkboxes are initially unchecked.\n")

        # 2. Are all checkboxes checked initially?
        print("Test 2: Are all checkboxes checked?")
        all_checked = all(checkbox.is_selected() for checkbox in checkboxes)
        if all_checked:
            print("All checkboxes are initially checked.\n")
        else:
            print("Not all checkboxes are initially checked.\n")

        # 3. Can the first checkbox be toggled?
        print("Test 3: Can the first checkbox be toggled?")
        first_checkbox = checkboxes[0]
        initial_state = first_checkbox.is_selected()
        first_checkbox.click()
        assert first_checkbox.is_selected() != initial_state, "First checkbox state did not change."
        print("First checkbox toggled successfully.\n")

        # 4. Can the second checkbox be toggled?
        print("Test 4: Can the second checkbox be toggled?")
        second_checkbox = checkboxes[1]
        initial_state = second_checkbox.is_selected()
        second_checkbox.click()
        assert second_checkbox.is_selected() != initial_state, "Second checkbox state did not change."
        print("Second checkbox toggled successfully.\n")

    except Exception as e:
        print(f"Error encountered during testing: {e}")

    finally:
        # Pause for observation (optional)
        time.sleep(2)
        # Close the browser
        driver.quit()

# Run the test
test_checkboxes()
