"""
Belongs: Functional Test
Author: Jinyu Chen
Email: jinyu2010.chen@gmail.com
Date: 26/05/2016
"""
    
import time
import unittest  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Testcases.BasicTestCase import BasicTestCase
from Objects.solutions import solutions_menu_list_objs


class SolutionsMenuDropdownListTestCase(BasicTestCase):
    
        
    def __init__(self, methodName='runTest'):
        BasicTestCase.__init__(self, methodName)
        self.be_tested_link = self.main_page + "/HP_SimplifiedConfig/"
    
    def testSolutionMenuDropdownListItems(self):
        
        '''
        test solutions sub menu list compared with data.
        '''
        
        self.web_driver.get(self.be_tested_link)
        # from home page click link until to tested page.
        expected_menu_list  = ['Transform to a Hybrid Infrastructure',
                                                'Protect Your Digital Enterprise',
                                                'Empower the Data-Driven Organization',
                                                'Cloud',
                                                'Security',
                                                'Big Data',
                                                'Mobility',
                                                'Infrastructure',
                                                'Internet of Things',
                                                'Small and Medium Business',
                                                'Service Providers',
                                                'All Solutions']
        
        solu_menu_link_obj = solutions_menu_list_objs.get_solustions_menu(self.web_driver)
        ActionChains(self.web_driver).move_to_element(solu_menu_link_obj).perform()
        time.sleep(1)
        self.take_screenshot('5.solutions_menu_dropdown_list.png')
        solu_drop_obj = solutions_menu_list_objs.get_dropdown(self.web_driver)
        solu_drop_li_objs = solu_drop_obj.find_elements_by_tag_name('li')
        
        # get all of li value when the value is not empty
        result_menu_list = [ li.text for li in solu_drop_li_objs if li.text]
        
        self.assertEqual(list(set(expected_menu_list) - set(result_menu_list)), [], \
                         "The Solutions Dropdown list does not match the expected reuslt.")
        
     
def suite():
    """
    test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
    """
    suite = unittest.TestSuite()
    suite.addTest(SolutionsMenuDropdownListTestCase("testSolutionMenuDropdownListItems"))
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite()) 
    