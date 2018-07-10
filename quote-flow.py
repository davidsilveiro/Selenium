""" Firefox webdriver required:               """
""" https://github.com/mozilla/geckodriver/   """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import csv
from time import sleep

class Quotesearch(unittest.TestCase):
    def setUp(self):
        """Hook onto driver"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        """Navigate to application"""
        self.driver.get("https://www.health-on-line.co.uk/quote/")

    def quote(self):
        """ Question: Do you currently have health insurance? (answer: No) """
        try:
            button_no_quote = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't find button_no_quote exiting")
            exit(0)

        """ Scroll into view of button_no_quote """
        self.driver.execute_script("arguments[0].scrollIntoView();", button_no_quote)

        """ Select button_no_quote """
        button_no_quote.click()

        """ Wait for continue to become available and click """
        try:
            phase_1_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button3"))
            )
        except:
            print("Couldn't find continue button for phase 1")
            exit(0)

        phase_1_continue.click()

        print("Successfully passed phase 1")
        print("Starting Phase 2")

        """Wait for postcode input field to become available"""

        try:
            postcode_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("unable to find postcode element")
            exit(0)

        """ Scroll into view of postcode input field """
        self.driver.execute_script("arguments[0].scrollIntoView();", postcode_elem)

        """Input our dummy postcode """
        postcode_elem.send_keys("BH8 8AQ")

        """ Wait for continue to become available and click """

        try:
            phase_2_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't find continue button for phase 2")
            exit(0)

        phase_2_continue.click()

        print("Successfully passed phase 2")
        print("Starting phase 3")

        """ Wait 1 element load and then populate all 3 DOB fields """
        try:
            dob_DD = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("Couldn't find DD field")
            exit(0)

        """ Scroll into view of day DOB field """
        self.driver.execute_script("arguments[0].scrollIntoView();", dob_DD)

        """ Day field """
        dob_DD.send_keys("03")
        """ Month Field """
        self.driver.find_element_by_id("input2").send_keys("03")
        """ Year Field """
        self.driver.find_element_by_id("input3").send_keys("1993")

        """ Wait for continue to become available and click """
        try:
            phase_3_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't find continue button for phase 3")
            exit(0)

        phase_3_continue.click()

        print("Successfully passed phase 3")
        print("Starting phase 4")

        """ Wait for Title field to load """
        try:
            title_field= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("Couldn't find title field")
            exit(0)

        """ Scroll to our title field """
        self.driver.execute_script("arguments[0].scrollIntoView();", title_field)

        """ Select our title via js injection by index """
        self.driver.execute_script("document.getElementById('input1').selectedIndex = 1")

        """Fill in our forename field """
        self.driver.find_element_by_id("input2").send_keys("test")
        """ Fill in our surname field """
        self.driver.find_element_by_id("input3").send_keys("test")


        """ Wait for continue to become available and click """
        try:
            phase_4_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't find continue button for phase 4")
            exit(0)

        phase_4_continue.click()

        print("Successfully passed phase 4")
        print("Starting phase 5")

        """ Wait for email field to load """
        try:
            email_field= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("Couldn't find email field")
            exit(0)
        
        """ Populate our email field """
        email_field.send_keys("test@test.com")

        """ Populate our mobile field """
        self.driver.find_element_by_id("input2").send_keys("07777777777")

        """ Wait for continue to become available and click """
        try:
            phase_5_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't find continue button for phase 5")
            exit(0)

        phase_5_continue.click()

        print("Successfully passed phase 5")
        print("Starting phase 6")

        """Question: Who is going to be on the policy?"""

        """Select 'just me' """

        try:
            justme = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("Couldn't locate just me option for phase 6")
            exit(0)

        justme.click()
       
        """ Wait for continue to become available and click """

        try:
            phase_6_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't locate continue button for phase 6")
            exit(0)

        phase_6_continue.click()

         print("Successfully passed phase 6")
        print("Starting phase 7")

        """ Question: past 4 years, person insured, had or received treatment for \
         the following conditions? """

        """ Select no"""
        try:
            no_phase_7 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "radioButton2"))
            )
        except:
            print("Couldn't find no button for phase 7")
            exit(0)

        no_phase_7.click()

        """ Question: Please confirm you have permission to give us \
         medical information from everyone over the age of 16 on the policy. """

        self.driver.find_element_by_id("radioButton5").click()


        """ Wait for continue to become available and click """

        try:
            phase_7_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "radioButton4"))
            )
        except:
            print("Couldn't locate continue button for phase 7")
            exit(0)

        phase_7_continue.click()

         
        print("Successfully passed phase 7")
        print("Starting phase 8")


        """ Question: Have you, or anyone to be insured on the policy,  \
        used any tobacco products within the last 12 months? """

        """ Select no """
        try:
            no_phase_8 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "radioButton2"))
            )
        except:
            print("Couldn't locate continue button for phase 8")
            exit(0)

        no_phase_8.click()


        try:
            phase_8_continue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button2"))
            )
        except:
            print("Couldn't locate continue button for phase 8")
            exit(0)

        phase_8_continue.click()


        print("Successfully passed phase 8")
        print("Starting phase 9")

        """ Question: When would you like your cover to start? """

         try:
            start_day = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input1"))
            )
        except:
            print("Couldn't locate start day for phase 9")
            exit(0)

        """ Day """
        start_day.send_keys("10")
        """ Month """
        self.driver.find_element_by_id("input2").send_keys("10")
        """ Year """
        self.driver.find_element_by_id("input3").send_keys("2018")

        """ Get Quote """
        self.driver.find_element_by_id("button2").click()


        """Finished quote flow """
        print("Finished quote flow")
        sleep(5)

    def shutdown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
	print("Starting our testing")
    unittest.main()