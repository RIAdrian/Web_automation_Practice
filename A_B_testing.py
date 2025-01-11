from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configure the Service for ChromeDriver
service = Service("...")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the A/B Testing page
driver.get("https://the-internet.herokuapp.com/abtest")

try:
    # 1. Check which variation of the page is displayed (A or B)
    # Retrieve the page heading to determine if the version is "Variation 1" (A) or "Control" (B).
    heading = driver.find_element(By.TAG_NAME, "h3").text
    if "A/B Test Variation 1" in heading:
        print("Variation 1 is displayed (Version A).")
    elif "A/B Test Control" in heading:
        print("Control version is displayed (Version B).")
    else:
        print("Unexpected version of the page is displayed.")
    
    # 2. Verify the content of the page
    # Ensure that the description text contains the expected keywords for split testing.
    description = driver.find_element(By.TAG_NAME, "p").text
    assert "split testing" in description, "Description does not contain the expected content."
    print("Page description is correct.")
    
    # 3. Verify the 'Elemental Selenium' link
    # Check that the link URL is correct and matches the expected destination.
    link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
    assert link.get_attribute('href') == "http://elementalselenium.com/", "Link URL is incorrect."
    print("Elemental Selenium link is correct.")
    
    # 4. Measure the page load time
    # Refresh the page to measure how long it takes to load.
    start_time = time.time()
    driver.refresh()
    load_time = time.time() - start_time
    print(f"Page loaded in {load_time:.2f} seconds.")
    
    # 5. Verify the footer content
    # Ensure the footer contains the expected text indicating it's powered by Elemental Selenium.
    footer = driver.find_element(By.TAG_NAME, "footer").text
    assert "Powered by Elemental Selenium" in footer, "Footer text is missing or incorrect."
    print("Footer is correct.")

except Exception as e:
    # Log any errors encountered during the test execution.
    print(f"Error encountered during testing: {e}")

# Pause for observation (optional)
time.sleep(5)

# Close the browser
driver.quit()
