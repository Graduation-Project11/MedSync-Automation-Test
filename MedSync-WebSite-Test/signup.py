# login_signup.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def Signup(driver, name, email, password, confirmPassword):
    try:
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        confirmPassword_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "confirmPassword"))
        )
        signup_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'Sign Up')]"))
        )

        # Clear any old values
        name_input.clear()
        email_input.clear()
        password_input.clear()
        confirmPassword_input.clear()
        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirmPassword_input.send_keys(confirmPassword)

        signup_button.click()
        print("Clicked on 'Sign Up' button and signed up.")

        # Check for the Email Verification element
        element_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Email Verification')]"))
        )
        time.sleep(10)
        if element_present:
            print("Sign up successfully. Email verification found.")
            return True
        else:
            print("Sign up successful but did not find the Email Verification element.")
            return False

    except Exception as e:
        print("Error signing up:", str(e))
        return False

