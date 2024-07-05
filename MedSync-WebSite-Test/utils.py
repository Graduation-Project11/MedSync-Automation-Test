# utils.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from login import login
from signup import Signup

def open_main_website(url,email,password):
    try:
        chrome_options = Options()
        driver_path = 'C:/Users/M/chromedriver.exe'  # Adjust this path to your ChromeDriver executable
        service = Service(driver_path)

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()

        driver.get(url)
        print("Main website opened successfully.")

        try:
            # Wait for the "About Us" button to be clickable and click it
            about_us_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'About Us')]"))
            )
            about_us_button.click()
            print("Navigated to 'About Us' section.")
            time.sleep(2)  # Adjust sleep time as needed
        except Exception as e:
            print("Error navigating to 'About Us' section:", str(e))

        try:
            # Wait for the "Explore" button to be clickable and click it
            explore_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Explore')]"))
            )
            explore_button.click()
            print("Navigated to 'Explore' section.")
            time.sleep(2)  # Adjust sleep time as needed
        except Exception as e:
            print("Error navigating to 'Explore' section:", str(e))

        try:
            # Wait for the "Sign Up" button to be clickable and click it
            sign_up_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Up')]"))
            )
            sign_up_button.click()
            print("Navigated to 'Sign Up' section.")
            time.sleep(2)  # Adjust sleep time as needed
        except Exception as e:
            print("Error navigating to 'Sign Up' section:", str(e))

        try:
            # Wait for the "Login" link to be clickable and click it
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ms-2.text-orange[href='/login']"))
            )
            login_link.click()
            print("Clicked on 'Login' link.")
            if login(driver, email, password):
                print("Scenario test completed successfully during login.")
            else:
                print("Scenario test failed during login.")
        except Exception as e:
            print("Error clicking on 'Login' link:", str(e))

        #sign up senario    
        # try:
        #     # Wait for the "Login" link to be clickable and click it
        #     signup_link = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ms-2.text-orange[href='/signup']"))
        #     )
        #     signup_link.click()
        #     print("Clicked on 'SignUp' link.")
        #     if Signup(driver,'test','test1@gmail.com','123456789','123456789'):
        #         print("Scenario test completed successfully during sign up.")
        #     else:
        #         print("Scenario test failed during sign up.")
        
    
        # except Exception as e:
        #     print("Error clicking on 'SignUp' link:", str(e))    

        return driver

    except Exception as e:
        print("Error opening main website:", str(e))
        return None

