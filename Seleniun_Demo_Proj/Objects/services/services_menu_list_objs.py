from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

SERVICES_A_ATTR_DICT = {'class' : 'dropdown-toggle menu_link',
                                                    'text' : 'Services'}


def get_services_menu(web_driver):
    try:
        serv_obj = web_driver.find_element_by_link_text(SERVICES_A_ATTR_DICT['text'])
    except NoSuchElementException, e:
        print 'The Menu Solutions cannot be find out with the text "%s with error info[%s], and try to use Class to find it again"' \
                        % (SERVICES_A_ATTR_DICT['text'], e)
        serv_obj = web_driver.find_elements(by = By.CLASS_NAME, value = SERVICES_A_ATTR_DICT['class'])
    else:
        return serv_obj
    
    
def get_dropdown(web_driver):
    dropdown_lists = web_driver.find_elements(by = By.CLASS_NAME, value = 'dropdown-menu')
    for item in dropdown_lists:
        if item.get_attribute('style') == 'display: block;':
            return item
    raise NoSuchElementException('There are no any dropdown menu display...')
        

    