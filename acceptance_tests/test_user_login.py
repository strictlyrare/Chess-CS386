from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestUserLogin(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome()  # Ensure you have installed ChromeDriver
        self.driver.get("http://localhost:8000/login")  # Replace with actual URL of your app

    def test_valid_user_login(self):
        driver = self.driver
        
        # Locate the input fields
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        
        # Enter valid credentials
        username_input.send_keys("valid_username")
        password_input.send_keys("valid_password")
        
        # Submit login
        password_input.send_keys(Keys.RETURN)
        
        # Wait for page load and verify URL or successful login indicator
        time.sleep(2)
        self.assertIn("dashboard", driver.current_url)

    def test_invalid_user_login(self):
        driver = self.driver

        # Locate the input fields
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        # Enter invalid credentials
        username_input.send_keys("invalid_username")
        password_input.send_keys("invalid_password")

        # Submit login
        password_input.send_keys(Keys.RETURN)

        # Wait for error message
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error-message")
        self.assertTrue(error_message.is_displayed())
        self.assertEqual(error_message.text, "Invalid username or password")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
