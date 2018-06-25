from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

"""Functionality out-line needed. Will apply before 26/07/2018"""

def main():

    driver = webdriver.Chrome('C:')
    driver.get('http://')

    result_List = []
    counter = 0

    try:
        select_team = Select(driver.find_element_by_id("evteam"))
        select_quantity = Select(driver.find_element_by_id("evtickets"))
        options_team = select_team.options
        options_quantity = select_quantity.options
        team_amount = len(options_team)

        while counter < team_amount:
            select_team = Select(driver.find_element_by_id("evteam"))
            select_quantity = Select(driver.find_element_by_id("evtickets"))
            options_team = select_team.options
            select_team.select_by_index(counter)
            team = select_team.options[counter].text
            element_click_Search = driver.find_element_by_name("xpath/").click()
            
            for test in driver.find_elements_by_class_name('result-name'):      
                result_List.append(test.text)

            result_List[:] = [item for item in result_List if item != '']
            result_List[:] = [item for item in result_List if item != '@']

            errors = False

            print("---------------- " + team + "------------------")

            for result in result_List:
                if team not in result:
                    print("Found " + result + " while searching for " + team + \
                          " (ignore if doing a all team search)")
                    
                    errors = True

            if errors == False:
                print("Success: ticket results match our search!")
            

            counter += 1
            result_List = []
            driver.get("")

    finally:
        print("We're all finished")

if __name__ == '__main__':
    main()
