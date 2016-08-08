"""
This is a demo of selenium testing for web.
Author: Jinyu Chen
Email: jinyu2010.chen@gmail.com
Date: 26/05/2016
"""

from selenium.webdriver.common.by import By


PROLIANT_DL_SERVERS = 'ProLiant DL Servers'
PROLIANT_DL100_SERVERS = 'ProLiant DL100 Servers'
HP_PROLIANT_DL320e_GEN8_V2_SERVER = 'HP ProLiant DL320e Gen8 v2 Server'


def get_proliant_dl_servers(web_driver):
    return web_driver.find_element_by_link_text(PROLIANT_DL_SERVERS)
    
    
def get_proliant_dl100_servers(web_driver):
    return web_driver.find_element_by_link_text(PROLIANT_DL100_SERVERS)
    
def get_hp_proliant_dl320e_gen8_v2_server(web_driver):
    return web_driver.find_element_by_link_text(HP_PROLIANT_DL320e_GEN8_V2_SERVER)
    
def get_customize_btn(web_driver):
    customzie_btns = web_driver.find_elements(by = By.CLASS_NAME, value='hp_btn')
    return customzie_btns[0]