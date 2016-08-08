"""
Belongs: Functional Test
Author: Jinyu Chen
Email: jinyu2010.chen@gmail.com
Date: 28/05/2016
"""

import time
import unittest  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Testcases.BasicTestCase import BasicTestCase
from Objects.services import services_menu_list_objs
from Functions import GetDataFromDB


class ServicesMenuDropdownListTestCase(BasicTestCase):
    
        
    def __init__(self, methodName='runTest'):
        BasicTestCase.__init__(self, methodName)
        self.be_tested_link = self.main_page + "/HP_SimplifiedConfig/"
    
    def testServicesMenuDropdownListItems(self):
        '''
        test services sub menu list compared with data from database.
        '''
        self.web_driver.get(self.be_tested_link)

        # get test data from db
        expected_menu_list = GetDataFromDB.getServiesMenuList()
        
        # get service menu and hover on to show submenu list
        serv_menu_link_obj = services_menu_list_objs.get_services_menu(self.web_driver)
        ActionChains(self.web_driver).move_to_element(serv_menu_link_obj).perform()
        time.sleep(1)
        # take screenshot when submenu is display
        self.take_screenshot('6.services_menu_dropdown_list.png')
        serv_drop_obj = services_menu_list_objs.get_dropdown(self.web_driver)
        serv_drop_li_objs = serv_drop_obj.find_elements_by_tag_name('li')
        
        # get all of li value when the value is not empty
        result_menu_list = [ li.text for li in serv_drop_li_objs if li.text]
        
        # expected menu list substract the result emnu list
        self.assertEqual(list(set(expected_menu_list) - set(result_menu_list)), [], \
                         "The Solutions Dropdown list does not match the expected reuslt.")
        
     
def suite():
    """
    test suite is a collection of test cases, test suites, or both. 
    It is used to aggregate tests that should be executed together.
    """
    suite = unittest.TestSuite()
    suite.addTest(ServicesMenuDropdownListTestCase("testServicesMenuDropdownListItems"))
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite()) 
    