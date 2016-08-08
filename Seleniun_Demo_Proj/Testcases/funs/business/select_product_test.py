"""
Belongs: Functional Test
Author: Jinyu Chen
Email: jinyu2010.chen@gmail.com
Date: 24/05/2016
"""

import time
import unittest  

from Testcases.BasicTestCase import BasicTestCase
from Objects.home import home_link_objs
from Objects.products import products_objs


class SelectProductFunsTestCase(BasicTestCase):
    
        
    def __init__(self, methodName='runTest'):
        BasicTestCase.__init__(self, methodName)
        self.be_tested_link = self.main_page + "/HP_SimplifiedConfig/"
    
    def testProductSelect(self):
        
        self.web_driver.get(self.be_tested_link)
        # from home page click link until to tested page.
        home_link_objs.get_proliant_dl_servers(self.web_driver).click()
        self.take_screenshot('1.get_proliant_dl_servers.png')
        home_link_objs.get_proliant_dl100_servers(self.web_driver).click()
        self.take_screenshot('2.get_proliant_dl100_servers.png')
        home_link_objs.get_hp_proliant_dl320e_gen8_v2_server(self.web_driver).click()
        self.take_screenshot('3.get_hp_proliant_dl320e_gen8_v2_server.png')
        home_link_objs.get_customize_btn(self.web_driver).click()
        time.sleep(1)
        self.take_screenshot('4.get_customize_btn.png')
       
        self.assertEqual(products_objs.get_config_untitle(self.web_driver).text, 
                                    'Untitled Configuration 1',
                                    'The Untitled Configuration 1 does not match with the expetected result.')
        self.assertEqual(products_objs.get_category_title(self.web_driver).text, 
                                    'HP DL580 Gen9 Configure-to-order Server',
                                    "The title of HP DL580 Gen9 Configure-to-order Server does not match with the expected result.")
        
     
def suite():
    """
    test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
    """
    suite = unittest.TestSuite()
    suite.addTest(SelectProductFunsTestCase("testProductSelect"))
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite()) 
    