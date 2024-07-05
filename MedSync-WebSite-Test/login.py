# login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from dashboard import test_doctor_dashboard



def login(driver, email, password):
    try:
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'Log In')]"))
        )

        # Clear any old values
        email_input.clear()
        password_input.clear()
        email_input.send_keys(email)
        password_input.send_keys(password)

        login_button.click()
        print("Clicked on 'Log In' button and logged in.")

        time.sleep(20)
        # Check for successful login by verifying presence of element MedSync
        element_present = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'MedSync')]"))
        )
        if element_present:
            print("Logged in successfully.")
            if test_doctor_dashboard(driver):
                print("Doctor dashboard test completed successfully.")
                return True
            else:
                print("Doctor dashboard test failed.")
                return False
        else:
            print("Login successful but did not find expected element.")
            return False

    except Exception as e:
        print("Error logging in:", str(e))
        return False
