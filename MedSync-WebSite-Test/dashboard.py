from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def test_doctor_dashboard(driver):
    try:
        def wait_and_click(xpath):
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print(f"Clicked on {xpath}.")

        def wait_for_element(xpath):
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element

        time.sleep(3)
        # Click on "Requests" link
        wait_and_click("//a[contains(@href, '/pendingreq')]")
        edit_element = wait_for_element("//th[contains(text(), 'Edit')]")
        if edit_element:
            print("Requests section verified successfully.")
        else:
            print("Failed to verify Requests section.")
            return False

        time.sleep(3)
        # Click on "Patients" link
        wait_and_click("//a[contains(@href, '/approvedreqs')]")
        patients_profile_element = wait_for_element("//p[contains(text(), \"Patient's Profile and History\")]")
        if patients_profile_element:
            print("Patients section verified successfully.")
        else:
            print("Failed to verify Patients section.")
            return False

        time.sleep(3)
        # Click on "History" button
        wait_and_click("//button[contains(text(), 'history')]")
        print("Clicked on 'History' button.")

        # Click on "Settings" link
        time.sleep(3)
        wait_and_click("//a[contains(@href, '/settings')]")
        personal_info_element = wait_for_element("//h4[contains(text(), 'Personal Information')]")
        time.sleep(3)
        if personal_info_element:
            print("Settings section verified successfully.")
            return True
        else:
            print("Failed to verify Settings section.")
            return False

    except TimeoutException as timeout_exception:
        print(f"Timeout waiting for element: {str(timeout_exception)}")
        return False
    except NoSuchElementException as no_such_element_exception:
        print(f"Element not found: {str(no_such_element_exception)}")
        return False
    except Exception as e:
        print("Error in testing doctor dashboard:", str(e))
        return False
