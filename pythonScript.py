from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_parking_bot():
    print("Bot logic started running!")

    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
    chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver"


    options = Options()
    options.binary_location = chrome_path
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)


    try:
        print("🔍 Launching Chrome...")
        driver.get('https://www.register2park.com/register')
        print("🔍 Launching Chrome...")
        time.sleep(2)

        driver.find_element(By.ID, 'propertyName').send_keys('inkwell')
        driver.find_element(By.ID, 'confirmProperty').click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-sm.select-property').click()
        driver.find_element(By.ID, 'registrationTypeVisitor').click()
        time.sleep(2)
        
        driver.find_element(By.ID, 'accessCode').send_keys('9181')
        driver.find_element(By.ID, 'propertyPassword').click()
        time.sleep(2)

        driver.find_element(By.ID, 'vehicleApt').send_keys('218')
        driver.find_element(By.ID, 'vehicleMake').send_keys('Toyota')
        driver.find_element(By.ID, 'vehicleModel').send_keys('Supra')
        driver.find_element(By.ID, 'vehicleLicensePlate').send_keys('DVH8788')
        driver.find_element(By.ID, 'vehicleLicensePlateConfirm').send_keys('DVH8788')
        driver.find_element(By.ID, 'vehicleInformation').click()
        time.sleep(2)

        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email-confirmation-view')))
        driver.find_element(By.ID, 'email-confirmation').click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'emailConfirmationEmailView'))
)
        # emailConfirmationEmailView is the field to enter email after clickintg on email-confirmation
        driver.find_element(By.ID, 'emailConfirmationEmailView').send_keys('rayanimani@gmail.com')
        driver.find_element(By.ID, 'email-confirmation-send-view').click()
        time.sleep(5)
    except Exception as e:
        print(f"Error occurred: {e}")





    finally:
        driver.quit()
