"""
This is a demo of selenium testing for web.
Author: Jinyu Chen
Email: jinyu2010.chen@gmail.com
Date: 26/05/2016
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

SOLUTONS_A_ATTR_DICT = {'class' : 'dropdown-toggle menu_link',
                                                    'text' : 'Solutions'}


def get_solustions_menu(web_driver):
    try:
        solu_obj = web_driver.find_element_by_link_text(SOLUTONS_A_ATTR_DICT['text'])
    except NoSuchElementException, e:
        print 'The Menu Solutions cannot be find out with the text "%s with error info[%s], and try to use Class to find it again"' \
                        % (SOLUTONS_A_ATTR_DICT['text'], e)
        solu_obj = web_driver.find_elements(by = By.CLASS_NAME, value=SOLUTONS_A_ATTR_DICT['class'])
    else:
        return solu_obj
    
    
def get_dropdown(web_driver):
    dropdown_lists = web_driver.find_elements(by = By.CLASS_NAME, value = 'dropdown-menu')
    for item in dropdown_lists:
        if item.get_attribute('style') == 'display: block;':
            return item
    raise NoSuchElementException('There are no any dropdown menu display...')
        

    