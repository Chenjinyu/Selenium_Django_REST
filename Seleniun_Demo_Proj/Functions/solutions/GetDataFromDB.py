from Libs import DatabaseMYSQL

SERVICES_MENU_SQL = 'SELECT * FROM data_for_services'


def getServiesMenuList():

    try:
        db_handler = DatabaseMYSQL()
    except Exception, e:
        print 'Cannot connect to MYSQL, Please check local mysql server status.'
        raise 
    
    meun_list = db_handler.get_rows(SERVICES_MENU_SQL)
    return [ item[1] for item in meun_list]