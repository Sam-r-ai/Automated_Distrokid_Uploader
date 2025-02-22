# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEndofdistrokidupload():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_endofdistrokidupload(self):
    self.driver.get("https://distrokid.com/new/")
    self.driver.set_window_size(1644, 979)
    self.driver.find_element(By.ID, "howManySongsOnThisAlbum").click()
    dropdown = self.driver.find_element(By.ID, "howManySongsOnThisAlbum")
    dropdown.find_element(By.XPATH, "//option[. = '10 songs']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-1-songwriter-1 .coolSelect").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, "#js-track-1-songwriter-1 .coolSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Music']").click()
    self.driver.find_element(By.NAME, "songwriter_real_name_first1").click()
    self.driver.find_element(By.NAME, "songwriter_real_name_first1").send_keys("Justin")
    self.driver.find_element(By.NAME, "songwriter_real_name_last1").click()
    self.driver.find_element(By.NAME, "songwriter_real_name_last1").send_keys("Cheung")
    self.driver.find_element(By.CSS_SELECTOR, "#js-copy-songwriters-link-1 div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-1 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-2 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-3 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-4 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-5 .dkRequiredForSpotify:nth-child(23) label:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-6 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-7 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-8 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-9 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.execute_script("window.scrollTo(0,27001)")
    self.driver.find_element(By.CSS_SELECTOR, "#js-track-table-10 .dkRequiredForSpotify:nth-child(23) label:nth-child(2) div:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mandatoryCheckboxYouTube .container-flex").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mandatoryCheckboxPromoServices .container-flex").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mandatoryAreyousurerecorded .radio-flex").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mandatoryAreyousureotherartist .container-flex").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mandatoryAreyousuretandc .container-flex").click()
    self.driver.find_element(By.ID, "doneButton").click()
  
