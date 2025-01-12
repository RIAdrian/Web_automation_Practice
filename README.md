# Web_automation_Practice
A comprehensive project to automate and test every interactive element available on The Internet Herokuapp. This repository aims to advance web automation skills by tackling diverse scenarios, including authentication, form handling, dynamic elements, and more.

# A/B Testing Automation Script

This script automates the testing of the **A/B Testing** page on [The Internet Herokuapp](https://the-internet.herokuapp.com/abtest). It is designed to validate the functionality and content of the A/B test variations, ensuring reliability and consistency across both versions of the page.

## Features

1. **Page Variation Detection**
   - Identifies whether the page displays "Variation 1" (Version A) or "Control" (Version B) by extracting and validating the page heading.

2. **Content Validation**
   - Ensures that the page description includes expected text about split testing, verifying its accuracy and relevance.

3. **Link Verification**
   - Confirms the presence of the "Elemental Selenium" link and checks that it correctly points to the expected external URL.

4. **Performance Measurement**
   - Measures the page load time during a refresh to monitor performance.

5. **Footer Consistency**
   - Validates that the footer contains the expected text: "Powered by Elemental Selenium."

## Purpose
This script is part of a broader web automation practice project. It demonstrates the use of **Selenium** to:
- Interact with web elements.
- Validate page content.
- Measure performance metrics.

By tackling A/B testing scenarios, this script lays the foundation for mastering automation testing techniques.

## Usage
1. Install the required dependencies:
   ```bash
   pip install selenium


# Add/Remove Elements Automation Script

This script automates the testing of the **Add/Remove Elements** page on [The Internet Herokuapp](https://the-internet.herokuapp.com/add_remove_elements/). The primary goal is to validate the functionality of adding and removing elements under various scenarios. Each test runs in isolation by restarting the browser to ensure a clean state.

## Features

1. **Add Elements**
   - The script allows adding one or more elements by clicking the "Add Element" button multiple times.

2. **Delete Elements**
   - The script ensures that all elements added can be deleted by clicking the "Delete" buttons.

3. **Test Isolation**
   - Each test starts with a fresh browser session to prevent state interference from previous tests.

4. **Assertions**
   - Assertions are used to validate the number of elements added or removed during the tests.

## Test Scenarios

### Test 1: Adding and Deleting a Single Element
- **Steps:**
  - Add one element.
  - Verify the element is added.
  - Delete the element.
  - Verify the element is deleted.
- **Expected Output:**
  - One element is added and successfully removed.

### Test 2: Adding 10 Elements
- **Steps:**
  - Add 10 elements.
  - Verify that all 10 elements are added.
- **Expected Output:**
  - 10 elements are added successfully.

### Test 3: Adding and Deleting 10 Elements
- **Steps:**
  - Add 10 elements.
  - Verify that all 10 elements are added.
  - Delete all 10 elements.
  - Verify that no elements remain.
- **Expected Output:**
  - 10 elements are added and successfully deleted.

### Test 4: Adding 50 Elements, Deleting 25, and Verifying the Remaining Count
- **Steps:**
  - Add 50 elements.
  - Verify that all 50 elements are added.
  - Delete the first 25 elements.
  - Verify that 25 elements remain.
- **Expected Output:**
  - 50 elements are added, 25 are deleted, and 25 remain.

## How to Run the Script

1. **Install Dependencies**
   - Ensure you have Python and Selenium installed.
   - Install Selenium using:
     ```bash
     pip install selenium
     ```

2. **Set Up ChromeDriver**
   - Download the appropriate version of ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Update the `Service` path in the script to point to your `chromedriver.exe`.

3. **Run the Script**
   - Execute the script in your terminal:
     ```bash
     python script_name.py
     ```

## Output
The script prints the results of each test scenario to the terminal, including success messages and any assertion errors if the tests fail.

## Notes
- **Test Isolation:** The script restarts the browser for each test to ensure a clean state.
- **Error Handling:** The script captures exceptions and prints error messages to the terminal for easier debugging.


# Basic Authentication Automation Script

This script automates the testing of the **Basic Authentication** page on [The Internet Herokuapp](https://the-internet.herokuapp.com/basic_auth). It handles both valid and invalid authentication scenarios using Selenium.

## Features

1. **Valid Credentials**
   - Tests successful authentication with the correct username and password.
   - Verifies that the success message (`"Congratulations!"`) appears after login.

2. **Invalid Credentials**
   - Tests authentication failure for:
     - Invalid username.
     - Invalid password.
     - No credentials provided.
     - Case-sensitive username and password.
   - Verifies that the authentication dialog or failure page is displayed as expected.

3. **Graceful Handling of Failures**
   - Includes checks for authentication failure by detecting the absence of success messages or expected page elements.
   - Prevents getting stuck on native browser dialogs.

## Test Scenarios Covered

### Test 1: Valid Username and Password
- **Input:** Username: `admin`, Password: `admin`.
- **Expected Outcome:** Authentication is successful, and the message `"Congratulations!"` is displayed.

### Test 2: Invalid Username
- **Input:** Username: `invalid_user`, Password: `admin`.
- **Expected Outcome:** Authentication fails, and the authentication dialog appears or the page does not load the success message.

### Test 3: Invalid Password
- **Input:** Username: `admin`, Password: `invalid_pass`.
- **Expected Outcome:** Authentication fails, and the authentication dialog appears or the page does not load the success message.

### Test 4: No Credentials Provided
- **Input:** No username or password in the URL.
- **Expected Outcome:** Authentication fails, and the browser displays an authentication dialog.

### Test 5: Case Sensitivity Check
- **Input:** Username: `Admin`, Password: `Admin` (incorrect case).
- **Expected Outcome:** Authentication fails, as credentials are case-sensitive.

## How to Run the Script

1. **Install Dependencies**
   - Ensure you have Python and Selenium installed.
   - Install Selenium using:
     ```bash
     pip install selenium
     ```

2. **Set Up ChromeDriver**
   - Download the appropriate version of ChromeDriver for your version of Chrome from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Update the `Service` path in the script to point to your `chromedriver.exe`.

3. **Run the Script**
   - Execute the script in your terminal:
     ```bash
     python basic_auth_tests.py
     ```

## Code Breakdown

1. **`start_driver_with_auth(username, password)`**
   - Launches the browser and navigates to the Basic Authentication page using credentials embedded in the URL.

2. **`verify_auth_success(driver)`**
   - Verifies that the authentication was successful by checking for the success message.

3. **`verify_auth_failure(driver)`**
   - Detects authentication failure by checking the absence of the success message or any expected page elements.

4. **Test Execution**
   - Each test starts with a fresh browser session to ensure test isolation.
   - Handles valid and invalid authentication scenarios gracefully.

## Expected Output

- **Test 1:** Logs `"Authentication successful with valid credentials."` in the terminal.
- **Test 2–5:** Logs `"Authentication failed as expected."` for invalid scenarios.

## Notes

- **URL-based Basic Authentication:**
  - Credentials are passed in the URL in the format: `https://username:password@site`.

- **Limitations:**
  - Selenium cannot directly interact with native browser authentication dialogs. This script bypasses that limitation by embedding credentials in the URL.

- **Error Handling:**
  - The script gracefully handles authentication failures and logs appropriate messages for debugging.




