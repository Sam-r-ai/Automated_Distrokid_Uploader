import os
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
unmastered_folder = "C:\\Users\\super\\Desktop\\Chinese symphonic"
download_folder = "C:\\Users\\super\\Downloads\\"
mastered_folder = "C:\\Users\\super\\Desktop\\Mastered"

song_array = []
def populateArray():
    global song_array
    for file_name in os.listdir(unmastered_folder):
        if file_name.lower().endswith('.mp3') and os.path.isfile(os.path.join(unmastered_folder, file_name)):
            song_array.append(file_name)

def save_cookies(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookies(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

def master_music():

    try:
        driver_path = 'C:/chromedriver-win64/chromedriver.exe'# Path to your ChromeDriver
        cookies_path = 'cookies.pkl'  # Path to save cookies

        chrome_options = Options()
        prefs = {
            "download.default_directory": "C:\\Users\\super\\Desktop\\Mastered",
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        # Initialize Chrome options
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--headless")  # Uncomment if you don't need a GUI
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--ignore-certificate-errors")

        # Initialize the ChromeDriver service
        service = Service(driver_path)

        # Initialize the ChromeDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the URL
        driver.get("https://distrokid.com/")

        # Load cookies
        try:
            load_cookies(driver, cookies_path)
            driver.refresh()
            time.sleep(3)  # Wait for the cookies to be applied and page to refresh
            print("Cookies loaded")
        except Exception as e:
            print(f"Could not load cookies: {e}")

        # Check if we are already logged in
        if "Upload & sell your music on Apple, Spotify, Amazon and YouTube Music | DistroKid" in driver.title:
            # Wait for the "Sign in" button to be clickable and click it
            sign_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "signInButtonFrontPage"))
            )
            sign_in_button.click()

            # Wait for the email input to be present, then fill it in
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputSigninEmail"))
            )
            email_input.send_keys("DISTROKIDEMAILHERE")

            # Fill in the password input
            password_input = driver.find_element(By.ID, "inputSigninPassword")
            password_input.send_keys("DISTROKIDPASSWORDHERE")

            # Submit the form
            password_input.send_keys(Keys.RETURN)

            print("Waiting for login")
            # Wait for the login to complete through 2fa and save cookies
            #time.sleep(20)
            WebDriverWait(driver, 10000).until(EC.title_contains("DistroKid"))
            save_cookies(driver, cookies_path)
            print("Cookies saved")

        # While songs are still in the folder, repeat this process of Music Mastering
        # Click on master music
        first_upload_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Master a track"))
        )
        first_upload_button.click()

        populateArray() #Adds all the songs from the unmastered file into the song_array

        # FOR LOOP to master all the tracks by repeating the same process



        #for song_name in song_array:
            #Upload track
            # Construct the full path of the song
        #    song_path = os.path.join(unmastered_folder, song_name)
    
            # Upload track
        #    WebDriverWait(driver, 15).until(
        #        EC.presence_of_element_located((By.ID, "fileToUpload"))
        #    ).send_keys(song_path)

        song_path = os.path.join(unmastered_folder, song_array[0])
        fileupload = driver.find_element(By.ID, "fileToUpload")
        
        fileupload.send_keys(song_path)
         # Wait for it to finish downloading
        download_button = WebDriverWait(driver, 500).until(
            EC.element_to_be_clickable((By.ID, "btnMixeaDownload"))
        )
        download_button.click()

        # DOWNLOAD THE NEW SONG FILE
        print("Waiting for download to complete")
        time.sleep(15)
        print("Attempting to click the first one")
        element = driver.find_element(By.CSS_SELECTOR, ".hover .hd-link-to-track .download-text")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Wait until the first HD download link is present
        #first_hd_download_link = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.CSS_SELECTOR, ".hd-link-to-track"))
        #)

        # Extract the href attribute
        #hd_download_url = first_hd_download_link.get_attribute("href")

        # Navigate to the HD download URL
        #driver.get(hd_download_url)



        #hd_option = WebDriverWait(driver, 15).until(
        #    EC.element_to_be_clickable((By.CLASS_NAME, "hd-li"))
        #)
        #hd_option.click()
        print("Download successful")
        #Abort the Program
        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    master_music()
