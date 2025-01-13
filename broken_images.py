from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# Configure the Service for ChromeDriver
service = Service("C:\\Users\\rente\\Downloads\\chromedriver-win64\\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the Broken Images page
driver.get("https://the-internet.herokuapp.com/broken_images")

# Function to check if images are loaded successfully
def check_broken_images():
    # Find all <img> elements on the page
    images = driver.find_elements(By.TAG_NAME, "img")
    total_images = len(images)
    broken_images = 0

    print(f"Total images found on the page: {total_images}")

    for img in images:
        img_src = img.get_attribute("src")
        print(f"Checking image: {img_src}")

        try:
            # Make a GET request to the image source
            response = requests.get(img_src)
            # Check if the status code is 200 (image loaded successfully)
            if response.status_code != 200:
                print(f"Broken image detected: {img_src} (Status Code: {response.status_code})")
                broken_images += 1
            else:
                print(f"Image loaded successfully: {img_src}")
        except Exception as e:
            print(f"Error checking image {img_src}: {e}")
            broken_images += 1

    print(f"\nSummary:")
    print(f"Total images: {total_images}")
    print(f"Broken images: {broken_images}")
    print(f"Working images: {total_images - broken_images}")

# Run the image check function
try:
    check_broken_images()
finally:
    # Close the browser
    driver.quit()
