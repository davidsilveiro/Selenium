""" Firefox webdriver required:               """
""" https://github.com/mozilla/geckodriver/   """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import csv

class HospitalSearch(unittest.TestCase):
    def setUp(self):
        """Hook onto driver"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        """Read postcodes via csv"""
        with open('post-code-file.csv', 'rb') as file_1:
            reader = csv.reader(file_1)
            postcodes = list(reader)

        """Navigate to application"""
        self.driver.get("https://www.health-on-line.co.uk/private-health-insurance/ \
        hospital-search")

    def search_for_postcode(self, postcodes):
        """ Loop through postcodes, submit and monitor if successful for storing in list """
        successful_codes = []
        for code in postcodes:

            """Wait for element load before scrolling into view via js (10 seconds)"""
            try:
    		    postcode_elem = WebDriverWait(self.driver, 10).until(
        	    EC.presence_of_element_located((By.ID, "ctl00$ctl00$ctl00$ContentPlaceHolderDefault$ \
                MasterContentPlaceHolder$ctl04$Widget_TreatmentNetwork_20$txtFindHospitalNear"))
    		    )
		    except:
			    print("postcode input field took to look to load, exiting")

			""" Scroll into element view """
            self.driver.execute_script("arguments[0].scrollIntoView();", postcode_elem)

            """ Submit code to field and fire search """
            postcode.send_keys(str(code))
            self.driver.find_element_by_name("ctl00$ctl00$ctl00$ContentPlaceHolderDefault$ \
            MasterContentPlaceHolder$ctl04$Widget_TreatmentNetwork_20$MapSearchBut").click()

            
            """ Wait for results (15 second timeout)"""
            try:
    		    postcode_elem = WebDriverWait(self.driver, 15).until(
        	    EC.presence_of_element_located((By.ID, "ContentPlaceHolderDefault_Master \
        	    ContentPlaceHolder_ctl04_Widget_TreatmentNetwork_20_searchResultsPanel"))
    		    )
    		    successful_codes.append(str(code))
		    except:
			    print("Postcode not found: "+str(code))

        """ Test Complete"""
        print("Completed all our postcodes""")
        print(successful_codes)

    def shutdown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
	print("Starting our testing")
    unittest.main()