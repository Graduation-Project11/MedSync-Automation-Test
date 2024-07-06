from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from helper_methods import smooth_scroll, click_wallet_info_button, click_manage_clinic_button,click_completed_button,click_canceled_button,click_pending_button,smooth_slight_scroll,click_Clinic_button,select_option_by_value,select_first_option_and_wait_for_second,AddClinic,click_profile_button



def test_doctor_dashboard(driver):
    try:
        def wait_and_click(xpath):
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print(f"Clicked on {xpath}.")

        def wait_for_element(xpath):
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element

        time.sleep(3)
        smooth_scroll(driver, down=True)
        time.sleep(3)  # Wait for 2 seconds
        
        # Scroll up smoothly
        smooth_scroll(driver, down=False)
        time.sleep(3)  # Wait for 2 seconds

        smooth_slight_scroll(driver, down=True)
        time.sleep(3)  # Wait for 2 seconds

        click_completed_button(driver)
        click_pending_button(driver)
        click_canceled_button(driver)
        

        smooth_slight_scroll(driver, down=False)
        time.sleep(3)  
       
        click_Clinic_button(driver)
        time.sleep(3)  

        smooth_slight_scroll(driver, down=True)
        time.sleep(3)  
        
        first_xpath = '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/select'  # XPath for the first <select> element
        second_xpath = '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/select'  # XPath for the second <select> element
        first_option_text = "Cairo"
        second_option_text = "Zamalek" 


        select_first_option_and_wait_for_second(driver, first_xpath, second_xpath, first_option_text, second_option_text)

        time.sleep(3) 
        AddClinic(driver)
        time.sleep(3) 

        smooth_slight_scroll(driver, down=False)
        time.sleep(3)  

        click_profile_button(driver)
        time.sleep(5)
        smooth_scroll(driver, down=True)
        time.sleep(2)
        smooth_scroll(driver, down=False)
        time.sleep(2)

        wait_and_click("//a[contains(@href, '/pendingreq')]")
        edit_element = wait_for_element("//th[contains(text(), 'Edit')]")

        smooth_scroll(driver, down=True)
        time.sleep(3)
        
        
        smooth_scroll(driver, down=False)
        time.sleep(3)
        if edit_element:
            print("Requests section verified successfully.")
        else:
            print("Failed to verify Requests section.")
            return False

        time.sleep(3)
     
        wait_and_click("//a[contains(@href, '/approvedreqs')]")
        patients_profile_element = wait_for_element("//p[contains(text(), \"Patient's Profile and History\")]")

        smooth_scroll(driver, down=True)
        time.sleep(3) 
        
        
        smooth_scroll(driver, down=False)
        time.sleep(3)  
        if patients_profile_element:
            print("Patients section verified successfully.")
        else:
            print("Failed to verify Patients section.")
            return False

        time.sleep(3)
       
        wait_and_click("//button[contains(text(), 'history')]")
        print("Clicked on 'History' button.")

        
        time.sleep(3)
        wait_and_click("//a[contains(@href, '/settings')]")
        personal_info_element = wait_for_element("//h4[contains(text(), 'Personal Information')]")
        time.sleep(3)
        if personal_info_element:
            print("Settings section verified successfully.")
            
            
            smooth_scroll(driver, down=True)
            time.sleep(3)  
            
       
            smooth_scroll(driver, down=False)
            time.sleep(3)  

           

            if click_manage_clinic_button(driver):
                
                print("Successfully clicked on 'Manage Clinic' button.")
                 
                smooth_scroll(driver, down=True)
                time.sleep(3) 
            
                smooth_scroll(driver, down=False)
                time.sleep(3)  

            else:
                print("Failed to click on 'Manage Clinic' button.")    

            if click_wallet_info_button(driver):
                
                print("Successfully clicked on 'Wallet Info' button.")

            else:
                print("Failed to click on 'Wallet Info' button.")
           
            

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
