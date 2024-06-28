import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def open_main_website(url):
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
            
            login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ms-2.text-orange[href='/login']"))
            )
            login_link.click()
            print("Clicked on 'Login' link.")
        
    
        except Exception as e:
            print("Error clicking on 'Login' link:", str(e)) 

            
        try:
            # Wait for the "Login" link to be clickable and click it
            signup_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ms-2.text-orange[href='/signup']"))
            )
            signup_link.click()
            print("Clicked on 'SignUp' link.")
            if Signup(driver,'rana','ranagaballah88@gmail.com','123456789','123456789'):
                print("Scenario test completed successfully during sign up.")
            else:
                print("Scenario test failed during sign up.")
        
    
        except Exception as e:
            print("Error clicking on 'SignUp' link:", str(e))         
        return driver

    except Exception as e:
        print("Error opening main website:", str(e))
        return None



























def Signup(driver,name, email, password, confirmPassword):
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
        print("Clicked on Log In button and logged in.")

        # Check for successful login by verifying presence of element MedSync
        element_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'MedSync')]"))
        )
        if element_present:
            print("Sign up successfully.")
            return True
        else:
            print("Sign up successful but did not find expected element.")
            return False

    except Exception as e:
        print("Error Signing up:", str(e))
        return False


if __name__ == "__main__":
   
    main_website_url = "https://medsync-doctor-website.netlify.app"
    
    open_main_website(main_website_url)
    







#  email = "ranagaballah88@gmail.com"
#     password = "123456789"
   #perform_scenario_test(main_website_url, login_url, email, password) 
# def login(driver, email, password):
#     try:
#         email_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "email"))
#         )
#         password_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "password"))
#         )
#         login_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//button[contains(text(), 'Log In')]"))
#         )

#         # Clear any old values
#         email_input.clear()
#         password_input.clear()
#         email_input.send_keys(email)
#         password_input.send_keys(password)

#         login_button.click()
#         print("Clicked on Log In button and logged in.")

#         # Check for successful login by verifying presence of element MedSync
#         element_present = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//h3[contains(text(), 'MedSync')]"))
#         )
#         if element_present:
#             print("Logged in successfully.")
#             return True
#         else:
#             print("Login successful but did not find expected element.")
#             return False

#     except Exception as e:
#         print("Error logging in:", str(e))
#         return False

# def perform_scenario_test(main_url, login_url, email, password):
#     main_driver = open_main_website(main_url)
#     if not main_driver:
#         print("Scenario test aborted due to main website opening error.")
#         return

#     try:
#         # Additional time to observe the main page
#         time.sleep(5)

#         # Close the main website
#         main_driver.quit()
#         print("Closed main website.")

#         # Open the login URL
#         login_driver = open_main_website(login_url)
#         if not login_driver:
#             print("Failed to open login URL. Scenario test aborted.")
#             return

#         if login(login_driver, email, password):
#             # Add additional steps or assertions here as needed after successful login
#             print("Scenario test completed successfully.")
#         else:
#             print("Scenario test failed during login.")
    
#     except Exception as e:
#         print("Scenario test encountered an unexpected error:", str(e))

#     finally:
#         if main_driver:
#             main_driver.quit()
#         if login_driver:
#             login_driver.quit()

