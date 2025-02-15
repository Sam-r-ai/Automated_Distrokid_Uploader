import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_cookies(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookies(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

def open_distrokid():
    try:
        # Path to your ChromeDriver
        driver_path = 'C:\\chromedriver-win64\\chromedriver.exe'  # Update this path
        cookies_path = 'distrokid_cookies.pkl'

        # Initialize Chrome options
        chrome_options = Options()
        # Add necessary options if needed
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--headless")  # Run headless if you don't need a GUI
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--ignore-certificate-errors")

        # Initialize the ChromeDriver service
        service = Service(driver_path)

        # Initialize the ChromeDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the URL
        driver.get("https://distrokid.com/")

        # Load cookies if available
        if os.path.exists(cookies_path):
            load_cookies(driver, cookies_path)
            driver.get("https://www.distrokid.com/mymusic")
            WebDriverWait(driver, 60).until(EC.title_contains("DistroKid"))
            print("Logged in using cookies, page title is:", driver.title)
        else:
            # Perform login if cookies are not available
            driver.get("https://www.distrokid.com/")
            WebDriverWait(driver, 60).until(EC.title_contains("Distrokid"))

            sign_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "signInButtonFrontPage"))
            )
            sign_in_button.click()

            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputSigninEmail"))
            )
            email_input.send_keys("your_email@example.com")

            password_input = driver.find_element(By.ID, "inputSigninPassword")
            password_input.send_keys("your_password")
            password_input.send_keys(Keys.RETURN)

            WebDriverWait(driver, 10).until(EC.title_contains("My Music"))
            save_cookies(driver, cookies_path)
            print("Logged in, page title is:", driver.title)

        # Sleep for 25 seconds
        time.sleep(25)

        # Click the "Upload music" button
        upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Upload music"))
        )
        upload_button.click()
        print("Navigated to the upload page")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    open_distrokid()




        # Select the secondary genre
