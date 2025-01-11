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
