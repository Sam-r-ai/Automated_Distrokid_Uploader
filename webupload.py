#A Selenium Script to automate browswer actions for logging in and uploading files

#Handle Authentication: Securely store and manage Distrokid credentials

import os
import pickle
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import date

today_date = date.today()
today_date = today_date.strftime("%Y-%m-%d")
#HERE I WANT IT TO 
upload_music_folder_path = "C:\\Users\\super\\Desktop\\OutputMusicFolder"
# Get how many songs
# Populate song name with OS get file get all the names

albumTitle = "Playful Robots"# CHANGE THIS TO MATCH ACTUAL ALBUM TITLE FROM INPUT
ready_to_upload = False
image_path = r"C:\Users\super\Desktop\GeneratedAlbumCovers\Playful Robots.png" #Change to format "albumcovertitle"


def save_cookies(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookies(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

def open_distrokid(albumTitle, ready_to_upload, image_path):
    song_names = [
        re.sub(r'\.mp3$', '', f, flags=re.IGNORECASE)
        for f in os.listdir(upload_music_folder_path)
        if os.path.isfile(os.path.join(upload_music_folder_path, f))
    ]
    songamount = len(song_names)
    print(f"Found {songamount} songs")
    try:
        driver_path = 'C:/chromedriver-win64/chromedriver.exe'# Path to your ChromeDriver
        cookies_path = 'cookies.pkl'  # Path to save cookies

        # Initialize Chrome options
        chrome_options = Options()
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

        # While songs are still in the folder, repeat this process of uploading
        # Click on upload
        first_upload_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Upload music"))
        )
        first_upload_button.click()

        print("Upload music button clicked")

        # Click Snapchat
        click_snapchat_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "chksnap"))
        )
        click_snapchat_button.click()
        click_swal2_confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
        )
        click_swal2_confirm.click()

        #Click Roblox
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "chkroblox"))
        )
        click_roblox_button.click()
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-chk-1"))
        )
        click_roblox_button.click()        
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-chk-2"))
        )
        click_roblox_button.click()        
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-chk-3"))
        )
        click_roblox_button.click()
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-chk-4"))
        )
        click_roblox_button.click()
        click_roblox_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
        )
        click_roblox_button.click()
        click_songAmount = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "howManySongsOnThisAlbum"))
        )
        click_songAmount.click()

        drop_down_song_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[. = '{songamount} songs']"))
        )
        drop_down_song_select.click()

        # Select Primary and Secondary Genre
        # PRIMARY
        # Select the primary genre
        genre_primary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "genrePrimary"))
        )
        genre_primary.click()

        genre_primary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[. = 'Electronic']"))
        )
        genre_primary.click()

        # Select the primary sub-genre
        sub_genre_primary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "subGenrePrimary"))
        )
        sub_genre_primary.click()
        sub_genre_primary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[. = 'Chill Out']"))
        )
        sub_genre_primary.click()

        # SECONDARY 
        genre_secondary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "genreSecondary"))
        )
        genre_secondary.click()
        genre_secondary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='genreSecondary']/option[. ='Hip Hop/Rap']"))
        )
        genre_secondary.click()
        print("HIP HOP CLICKED \n")

        #SELECT UPLOAD DATE 
        upload_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "release-date-dp"))
        )
        upload_date.click()
        # Wait for the calendar to appear and locate the 'Today' button
        upload_date.send_keys("2024-11-30")
        #ALBUM ARTWORK
        #album_image = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.CLASS_NAME, "artworkWrapped"))
        #)
        print("ALBUM IMAGE FOUND")
        #album_image.click()
        #print("ALBUM COVER CLICKED")
        artwork = driver.find_element(By.ID, "artwork")
        
        print("ALBUM ELEMENT FOUND, ATTEMPING UPLOAD ")
        artwork.send_keys(image_path)

        #Album Title
        album_title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "albumTitleInput"))
        )
        album_title.click()

        album_title.send_keys(albumTitle)

        #################### INPUTTING SONG TITLES ########################

        for idx, song_name in enumerate(song_names, start=1):
            print("attempting to upload song {idx}")
            # Enter track title
            song_title_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='Track {idx} title']"))
            )
            song_title_input.click()
            song_title_input.send_keys(song_name)
            print(f"Successfully named song {idx}")
            # UPLOADING MUSIC TO DISTROKID
            print("Attempting to upload song")
            music_file = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, f"js-track-upload-{idx}"))
            )
            print("Track upload file found.")
            path_to_music = f"C:\\Users\\super\\Desktop\\OutputMusicFolder\\{song_name}.mp3"
            music_file.send_keys(path_to_music)
            print("Track upload file complete")
            print("trying to click music only does not contain lyrics")
            #Click the music only does not contain lyrics
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#js-track-table-{idx} .dkRequiredForSpotify:nth-child(21) label:nth-child(2) div:nth-child(2)"))
            ).click()
            print("music only click successful attempting next upload")


        ######## FILL IN SONGWRITER INFORMATION  ################
        print("Attempting songwriter info upload")
        songwriter_info = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-track-1-songwriter-1 .coolSelect"))
        )
        songwriter_info.click()
        print("Songwriter button found trying to change to Music only")

        songwriter_info = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[. = 'Music']"))
        )
        songwriter_info.click()
        print("Music button only clicked now attempting to songwriter name")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, f"songwriter_real_name_first1"))
        ).send_keys("Justin")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, f"songwriter_real_name_last1"))
        ).send_keys("Cheung")
        print("Successfully entered songwriter details")
        print("Copying name to all")
        WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-copy-songwriters-link-1 div:nth-child(2)"))
        ).click()
        WebDriverWait(driver,10).until(# CLICKS ARE YOU SURE
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
        ).click()
        WebDriverWait(driver,10).until( #CLICKS CONFIRM
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
        ).click()
        # CLICK THE UPLOAD CHECKLISTS
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryCheckboxYouTube .container-flex"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryCheckboxPromoServices .container-flex"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryAreyousurerecorded .radio-flex"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryAreyousureotherartist .container-flex"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryAreyousuretandc .container-flex"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mandatoryCheckboxSnap b"))
        ).click()
        #Sometimes the non_standard checkbox is there, sometimes its not
        try:
            non_standard_caps_checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#nonStandardCapsCheckbox .container-flex"))
            )
            non_standard_caps_checkbox.click()
            print("Clicked non-standard caps checkbox")
        except:
            print("Non-standard caps checkbox not found, proceeding without it")

        #TIME TO CLICK UPLOAD!
        if(ready_to_upload):
            WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "doneButton"))
            ).click()


        # While loop for after first submission
        #WebDriverWait(driver, 120).until(
        #    EC.text_to_be_present_in_element(
        #        (By.XPATH, "//div[contains(text(), \"That was easy, wasn't it?\")]"),
        #        "That was easy, wasn't it?"
        #    )
        #)
        #driver.quit()

        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    open_distrokid(albumTitle, ready_to_upload, image_path)