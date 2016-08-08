"""
DatabaseMYSQL inherit basic library DatabaseCore. 
Author: jinyu2010.chen@gmail.com
Date: 05/27/2016
"""

from DatabaseCore import DatabaseCore
from Libs.Config import ParserConfigFile


class DatabaseMYSQL(DatabaseCore):
            
    def __init__(self): 
        
        account_section = 'TEST_MYSQL'
        
        read_config = ParserConfigFile(DatabaseCore.get_common_db_config_full_path())
        db_config_list = read_config.get_items_list(account_section)
        db_config_list.extend(['3306', 'mysql'])
        
        DatabaseCore.__init__(self, *db_config_list)
        
    
if __name__ == "__main__":   
    test = DatabaseMYSQL()
    print test.get_rows('SELECT * FROM data_for_services')