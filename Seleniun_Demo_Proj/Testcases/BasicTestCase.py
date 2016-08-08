from os import makedirs
from os.path import dirname, join, abspath,exists

import unittest  
from selenium import webdriver   

from Libs import Settings
from Libs import CommonFuns
from Libs import ParserConfigFile


class BasicTestCase(unittest.TestCase):
    
    """
    BasicTestCase
    Author: jinyu2010.chen@gmail.com
    Date: 05/27/2016
    """
    
    def __init__(self, methodName='runTest', web_driver = 'chrome'):
        unittest.TestCase.__init__(self, methodName) 
        self.web_driver_option = web_driver
        self.main_page = "http://127.0.0.1:8000"
        config_handler = ParserConfigFile(self.get_common_testcase_config_full_path())
        web_driver_item = 'WEB_DRIVER_' + self.web_driver_option.upper()
        try:
            web_driver_dict = config_handler.get_items_dict(web_driver_item)
            self.web_driver_name = web_driver_dict['web_driver_name']
            self.web_driver_path = web_driver_dict['web_driver_path']
        except Exception, e:
            raise AssertionError('There is no %s in the config file with the detail info: %s' % (web_driver_item,e ))
        
    
    def setUp(self):
        """
        setUp is same as precondtion of TestCase. the funciton is invoked automatically.
        """
        if self.web_driver_name == 'Chrome':
            from selenium.webdriver.chrome.options import Options
            chromeOptions = Options()
            chromeOptions.add_argument("--kiosk")
            self.web_driver = webdriver.Chrome(self.web_driver_path, chrome_options = chromeOptions)
        elif self.web_driver_name == 'Firefox':
            self.web_driver = webdriver.Firefox()
            self.web_driver.maximize_window()
        else:
            self.web_driver = None
            
        if not self.web_driver:
            raise AssertionError('We cannot create a web driver, please check your config file.')
        
        
    def tearDown(self):
        """
        tearDown do the round-off work, the function is invoked automatically.
        """
        self.web_driver.quit()  
        
        
    def take_screenshot(self, screenshot_name):
        screenshot_name_with_date = '.'.join(screenshot_name.split('.')[:-1]) + \
                                                    '_' + CommonFuns.get_current_date() + '.png'
        screenshot_path = join(CommonFuns.get_project_root(), Settings.LOG_PATH, \
                                                    CommonFuns.get_current_script_name(), Settings.SCREEN_SHOTS_FOLDER)
        print screenshot_path
        if not exists(screenshot_path):
            makedirs(screenshot_path)
        screenshot_path_with_name = join(screenshot_path, screenshot_name_with_date)
        print screenshot_path_with_name
        self.web_driver.get_screenshot_as_file(screenshot_path_with_name) 
        

    def get_common_testcase_config_full_path(self):
        #get current python file path, not current execute file path
        current_path = dirname(abspath(__file__))[:-10]
        return join(current_path, 'Libs/' + Settings.COMMON_TESTCASE_CONF_PATH)

