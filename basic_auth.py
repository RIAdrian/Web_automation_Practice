from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the Service for ChromeDriver
service = Service("C:\\Users\\rente\\Downloads\\chromedriver-win64\\chromedriver.exe")

# Function to start a WebDriver instance with authentication
def start_driver_with_auth(username, password):
    # Include username and password in the URL for basic authentication
    auth_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    driver = webdriver.Chrome(service=service)
    driver.get(auth_url)
    return driver

# Function to verify success message
def verify_auth_success(driver):
    try:
        # Wait for the success message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        message = driver.find_element(By.TAG_NAME, "p").text
        assert "Congratulations!" in message, "Authentication failed unexpectedly."
        print("Authentication successful with valid credentials.")
    except Exception as e:
        print(f"Error verifying authentication success: {e}")

# Function to check for authentication failure
def verify_auth_failure(driver):
    try:
        # Wait to ensure the page did not load successfully
        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        print("Authentication failed as expected.")
    except Exception:
        print("Unexpected behavior: Authentication failure not detected properly.")

# Test cases for Basic Auth
def test_basic_auth():
    try:
        # 1. Test: Valid username and password
        print("Test 1: Valid username and password")
        driver = start_driver_with_auth("admin", "admin")  # Use valid credentials
        verify_auth_success(driver)
        driver.quit()

        # 2. Test: Invalid username
        print("\nTest 2: Invalid username")
        driver = start_driver_with_auth("invalid_user", "admin")  # Invalid username
        verify_auth_failure(driver)
        driver.quit()

        # 3. Test: Invalid password
        print("\nTest 3: Invalid password")
        driver = start_driver_with_auth("admin", "invalid_pass")  # Invalid password
        verify_auth_failure(driver)
        driver.quit()

        # 4. Test: No credentials provided
        print("\nTest 4: No credentials provided")
        driver = webdriver.Chrome(service=service)
        driver.get("https://the-internet.herokuapp.com/basic_auth")  # No credentials in URL
        verify_auth_failure(driver)
        driver.quit()

        # 5. Test: Case sensitivity
        print("\nTest 5: Case sensitivity check")
        driver = start_driver_with_auth("Admin", "Admin")  # Incorrect case
        verify_auth_failure(driver)
        driver.quit()

    except Exception as e:
        print(f"Error encountered during testing: {e}")

# Run the tests
test_basic_auth()
