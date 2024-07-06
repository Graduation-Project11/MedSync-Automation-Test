import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def smooth_scroll(driver, down=True, duration=1):
    """Scrolls the webpage smoothly."""
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_by = scroll_height // 10 
    
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
    scroll_by = scroll_height // 30  
    
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
      
        manage_clinic_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/button[2]'))
        )
        
        
        manage_clinic_button.click()
        print("Clicked on 'Manage Clinic' button.")
        time.sleep(3)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Manage Clinic' button: {str(e)}")
        return False

def click_wallet_info_button(driver):
    try:
       
        wallet_info_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/button[3]'))
        )
        
        wallet_info_button.click()
        print("Clicked on 'Wallet Info' button.")
        time.sleep(2)

        smooth_scroll(driver, down=True)
        time.sleep(2)  
        
        
        smooth_scroll(driver, down=False)
        time.sleep(2) 
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Wallet Info' button: {str(e)}")
        return False        

def click_completed_button(driver):
    try:
        
        completed_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[2]'))
        )
        
        completed_button.click()
        print("Clicked on 'Completed' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Completed' button: {str(e)}")
        return False  


def click_pending_button(driver):
    try:
   
        pending_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[3]'))
        )
   
        pending_button.click()
        print("Clicked on 'Pending' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Pending' button: {str(e)}")
        return False  


def click_canceled_button(driver):
    try:
       
        canceled_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/button[4]'))
        )
        
  
        canceled_button.click()
        print("Clicked on 'Canceled' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Canceled' button: {str(e)}")
        return False  


def click_Clinic_button(driver):
    try:
        
        Clinic_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/button[2]'))
        )
        
   
        Clinic_button.click()
        print("Clicked on 'Clinic' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'Clinic' button: {str(e)}")
        return False


def click_profile_button(driver):
    try:
       
        profile_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[5]/div[2]/button'))
        )
        
        profile_button.click()
        print("Clicked on 'profile' button.")
        time.sleep(2)
        return True
    
    except Exception as e:
        print(f"Error clicking on 'profile' button: {str(e)}")
        return False

def select_option_by_value(driver, xpath, value):
    try:
       
        select_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        select = Select(select_element)
        select.select_by_value(value)
        
        print(f"Option '{value}' selected in the dropdown.")
        return True
    
    except Exception as e:
        print(f"Error selecting the option '{value}': {str(e)}")
        return False





def select_option_by_visible_text(driver, xpath, text):
    try:
       
        select_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
  
        select = Select(select_element)
        select.select_by_visible_text(text)
        
        print(f"Option '{text}' selected in the dropdown.")
        return True
    
    except Exception as e:
        print(f"Error selecting the option '{text}': {str(e)}")
        return False

def select_first_option_and_wait_for_second(driver, first_xpath, second_xpath, first_option_text, second_option_text):
    try:
        
        if not select_option_by_visible_text(driver, first_xpath, first_option_text):
            return False
        
     
        WebDriverWait(driver, 20).until(
            lambda driver: len(driver.find_elements(By.XPATH, f"{second_xpath}/option")) > 1
        )
        
        
        if not select_option_by_visible_text(driver, second_xpath, second_option_text):
            return False
        
        print(f"Option '{second_option_text}' selected in the second dropdown.")
        return True

    except Exception as e:
        print(f"Error in selecting options: {str(e)}")
        return False



def AddClinic(driver):
    try:
        street_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/input[1]'))
        )
        desc_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/input[2]'))
        )
        duration_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/input[3]'))
        )
        checkupPrice_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/input[4]'))
        )
        followupPrice_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/input[5]'))
        )

        workDays_button =WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='mt-3 btn btn-primary' and text()='+']"))
        )

        
        street_input.clear()
        desc_input.clear()
        duration_input.clear()
        checkupPrice_input.clear()
        followupPrice_input.clear()
        street_input.send_keys('698 Barney Canyon Apt. 772')
        desc_input.send_keys('Omnis sint ut ratione consequatur et et placeat. Consequatur quam deserunt et officia voluptatem et. Enim sit ipsam provident ex non.')
        duration_input.send_keys(15)
        checkupPrice_input.send_keys(500)
        followupPrice_input.send_keys(1000)
        time.sleep(3)  
        workDays_button.click()
        time.sleep(3)  
        smooth_slight_scroll(driver, down=True)
        time.sleep(3)  

        try: 
            select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "day-0"))
            )
            
            select = Select(select_element)
            select.select_by_value("Monday")
            
            print(f"Option 'Monday' selected in the dropdown.")

        except Exception as e:
            print(f"Error selecting the option 'Monday': {str(e)}")

        time.sleep(3)  

        startHour_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/input[1]'))
        )
        endHour_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/input[2]'))
        )

        send_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[2]/button'))
        )
        
        startHour_input.clear()
        endHour_input.clear()
        startHour_input.send_keys('7:00 AM')
        endHour_input.send_keys('8:00 AM')
        send_button.click()
        time.sleep(5)

        print("Clicked on 'Sent' button and add clinic.")
    except Exception as e:
        print("Error add clinic:", str(e))
        return False


def click_profile_button(driver):
    try:
      
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[5]/div[2]/button'))
        )
        
        
        button.click()
        print("Clicked on 'Profile' button.")
        time.sleep(3)
        
    
    except Exception as e:
        print(f"Error clicking on 'Profile' button: {str(e)}")
       

