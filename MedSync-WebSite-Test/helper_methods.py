import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def smooth_scroll(driver, down=True, duration=1):
    """Scrolls the webpage smoothly."""
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_by = scroll_height // 10  # Adjust this value to make scrolling smoother
    
    if down:
        for i in range(0, scroll_height, scroll_by):
            driver.execute_script(f"window.scrollBy(0, {scroll_by});")
            time.sleep(duration / 10)
    else:
        for i in range(scroll_height, 0, -scroll_by):
            driver.execute_script(f"window.scrollBy(0, -{scroll_by});")
            time.sleep(duration / 10)


def smooth_slight_scroll(driver, down=True, duration=1):
    """Scrolls the webpage smoothly."""
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_by = scroll_height // 30  # Adjust this value to make scrolling smoother
    
    if down:
        for i in range(0, scroll_height, scroll_by):
            driver.execute_script(f"window.scrollBy(0, {scroll_by});")
            time.sleep(duration / 30)
    else:
        for i in range(scroll_height, 0, -scroll_by):
            driver.execute_script(f"window.scrollBy(0, -{scroll_by});")
            time.sleep(duration / 30)

def click_manage_clinic_button(driver):
    try:
        # Find the button element using the exact XPath
        manage_clinic_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/button[2]'))
        )
        
        # Click the button
        manage_clinic_button.click()
        print("Clicked on 'Manage Clinic' button.")
        time.sleep(3)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Manage Clinic' button: {str(e)}")
        return False

def click_wallet_info_button(driver):
    try:
        # Find the button element using the exact XPath
        wallet_info_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/button[3]'))
        )
        
        # Click the button
        wallet_info_button.click()
        print("Clicked on 'Wallet Info' button.")
        time.sleep(2)
        # Scroll down smoothly
        smooth_scroll(driver, down=True)
        time.sleep(2)  # Wait for 2 seconds
        
        # Scroll up smoothly
        smooth_scroll(driver, down=False)
        time.sleep(2)  # Wait for 2 seconds
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Wallet Info' button: {str(e)}")
        return False        

def click_completed_button(driver):
    try:
        # Find the button element using the exact XPath
        completed_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[2]'))
        )
        
        # Click the button
        completed_button.click()
        print("Clicked on 'Completed' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Completed' button: {str(e)}")
        return False  


def click_pending_button(driver):
    try:
        # Find the button element using the exact XPath
        pending_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[3]'))
        )
        
        # Click the button
        pending_button.click()
        print("Clicked on 'Pending' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Pending' button: {str(e)}")
        return False  


def click_canceled_button(driver):
    try:
        # Find the button element using the exact XPath
        canceled_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[4]'))
        )
        
        # Click the button
        canceled_button.click()
        print("Clicked on 'Canceled' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Canceled' button: {str(e)}")
        return False  


def click_Clinic_button(driver):
    try:
        # Find the button element using the exact XPath
        Clinic_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/button[2]'))
        )
        
        # Click the button
        Clinic_button.click()
        print("Clicked on 'Clinic' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Clinic' button: {str(e)}")
        return False


def click_profile_button(driver):
    try:
        # Find the button element using the exact XPath
        profile_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[5]/div[2]/button'))
        )
        
        # Click the button
        profile_button.click()
        print("Clicked on 'profile' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'profile' button: {str(e)}")
        return False

def select_first_option(driver, xpath):
    try:
        # Locate the <select> element using XPath
        select_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Create a Select object from the located <select> element
        select = Select(select_element)
        
        # Select the first option by index (index 0)
        select.select_by_index(0)
        
        print("First option selected in the dropdown.")
        return True
    
    except Exception as e:
        print(f"Error selecting the first option: {str(e)}")
        return False

