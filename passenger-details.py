from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def extras(pax,driver):

    """ DATA """

    extras_Total_Price = driver.find_element_by_class_name("texSubTotal")
    driver.execute_script("arguments[0].scrollIntoView();", extras_Total_Price)
  
    print extras_Total_Price.text

    extras_Points = driver.find_element_by_class_name("pts-value").text
    extras_test = driver.find_element_by_css_selector(".region-xsltcontainer .region-xsl-flt .result-fltroute").text

    print extras_Total_Price
    print extras_Points
 

    ######## GET PRODUCT SUMMARY INFO ##########

    ############################################

    """ Loop through and fill contact details """

    loop_Var = 0

    while loop_Var < pax:
        
        pax_ID       =   "paxTitle" + str(loop_Var)
        pax_Name     =   "paxFName" + str(loop_Var)
        pax_Middle   =   "paxMName" + str(loop_Var)
        pax_Surname  =   "paxSName" + str(loop_Var)
        pax_age_M    =   "paxDOBM"  + str(loop_Var)
        pax_age_D    =   "paxDOBD"  + str(loop_Var)
        pax_age_Y    =   "paxDOBY"  + str(loop_Var)


        ID_Element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, pax_ID))
    )
        driver.execute_script("arguments[0].scrollIntoView();", ID_Element)

        name_Element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, pax_Name))
    )

        driver.execute_script("arguments[0].scrollIntoView();", name_Element)

        """ Fill in name details """

        name_Element.send_keys("test" + str(loop_Var))
        d.find_element_by_id(pax_Middle).send_keys("test" + str(loop_Var))
        d.find_element_by_id(pax_Surname).send_keys("test" + str(loop_Var))
        
        """ Fill in ages """

        select = Select(driver.find_element_by_name(pax_age_M))

        select.select_by_value('03')

        select = Select(driver.find_element_by_name(pax_age_D))
        select.select_by_value('3')

        select = Select(driver.find_element_by_name(pax_age_Y))
        select.select_by_value('1995')

        """ Email address """
        driver.find_element_by_name("emailAddress").send_keys("test@test.com")

        loop_Var += 1

def main():
    print("Starting..."
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    driver = webdriver.Firefox(capabilities=cap)
    pax = 4
    extras(driver, pax)

if __name__ == "__main__":
    main()
