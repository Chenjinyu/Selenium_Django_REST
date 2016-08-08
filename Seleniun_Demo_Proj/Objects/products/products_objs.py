UNTITLE_CONFIG_ID = 'untitled_title'
CGR_LOADED_TITLE_XPATH = "//div[@id='cgr_loaded']/h3"
PROCESSER_TEXT = 'Processer'
MEMORY_TEXT = 'Memory'
STORAGE_TEXT = 'Storage'

def get_config_untitle(web_driver):
    return web_driver.find_element_by_id(UNTITLE_CONFIG_ID)


def get_category_title(web_driver):
    return web_driver.find_element_by_xpath(CGR_LOADED_TITLE_XPATH)


def get_processer(web_driver):
    return web_driver.find_element_by_link_text(PROCESSER_TEXT)
      
        
def get_memory(web_driver):
    return web_driver.find_element_by_link_text(MEMORY_TEXT)


def get_storage(web_driver):
    return web_driver.find_element_by_link_text(STORAGE_TEXT)
