from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main():

	cap = DesiredCapabilities().FIREFOX
	cap["marionette"] = False
	browser = webdriver.Firefox(capabilities=cap)
   
	urls = ['']
	
	##### Homepage ####
	browser.get('http://')

	### fullscreen ###
	browser.maximize_window()
	browser.save_screenshot('firefox-screenshots/fullscreen-homepage.png')

	### tablet ###
	browser.set_window_size('768', '1024')
	browser.save_screenshot('firefox-screenshots/tablet-homepage.png')

	### mobile ###
	browser.set_window_size('360', '640')
	browser.save_screenshot('firefox-screenshots/phone-homepage.png')


	#### Loop through urls and take screenshots at different resolutions ###

	c = 0
	for link in urls:
		print("Full Screenshot of: " + link + ' complete!')
		browser.get('http://' + link)

		### fullscreen ###
		browser.maximize_window()
		browser.save_screenshot('firefox-screenshots/fullscreen-' + str(c) + '.png')

		### tablet ###

		print("tablet Screenshot of: " + link + ' complete!')
		browser.set_window_size('768', '1024')
		browser.save_screenshot('firefox-screenshots/tablet-' + str(c) + '.png')

		### mobile ###

		print("mobile Screenshot of: " + link + ' complete!')
		browser.set_window_size('360', '640')
		browser.save_screenshot('firefox-screenshots/phone-' + str(c) + '.png')

		c += 1
	

	##### Search-types [result pages only] ####

	### FLIGHTS ###

	#browser.get('')
	#browser.execute_script("teswitchsearchtype(1, $('input[name=\'tsb-subtype-1\']:checked').val());")

	#origin = browser.find_element_by_id("originid")
	#browser.execute_script("arguments[0].value = '11665;LON;11665';", origin) 

	#############################################

	url_Searchtypes = [""]
	x = 0
	y = 0
	for urls in url_Searchtypes:
		print("Screenshot of: " + urls + "Complete!")
		browser.get(urls)
		browser.maximize_window()
		browser.save_screenshot('firefox-screenshots/searchtype-test' + str(x) +'.png')
		timeout = 15
		try:
			element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.result-name-title'))
			WebDriverWait(browser,timeout).until(element_present)
			browser.save_screenshot('firefox-screenshots/searchtype-element-wait' + str(y) +'.png')
			y += 1
		except TimeoutException:
			browser.save_screenshot('firefox-screenshots/searchtype-element-wait' + str(y) +'.png')
	    	print "Timed out waiting for page to load"
	    	y += 1
        y += 1
        x += 1

if __name__ == '__main__':
	main()