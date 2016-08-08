"""
DatabaseCore is a core library for database operations.
    
Python database library SQLAlchemy is used: http://www.sqlalchemy.org/
Default driver is Microsoft SQL Server 

Use this class to implement more specific database class (inheritance or composition). 
Author: jinyu2010.chen@gmail.com
Date: 05/27/2016
"""

import sqlalchemy
from os.path import join, dirname, abspath

from Libs import Settings

class DatabaseCore(object):
    
    def __init__(self, 
                 host = None, # Hostname or ip address of database
                 username = None, # Username for login the database
                 password = None, # Password for login the database
                 database = None, # Database name
                 port = None, # port for host
                 driver = None,# Dialect, select one of: sqlite, mysql, postgres, oracle, myssql or firebird
                 charset = 'utf8'): 
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.driver = driver
        self.charset = charset
        self._engine = None
        self._conn   = None
   
        # Make connection if credentials given in constructor
        if self.host is not None:
            if self.username is None or self.password is None:
                print "**[ERROR]** Username and Password not given!"
                raise Exception("**[ERROR]** Username and Password not given!")
            else:
                self.connect()
                
    def __del__(self):
        try:
            if self._conn is not None:
                self._conn.close()
            if self._engine is not None:
                self._engine.dispose()
        except Exception, e:
            print "**[ERROR]** error happen in __del__: %s" %e
        print "**[INFO]** DB connection closed at the end..."
        
    def connect(self): 
        """Connect to database with relevant database parameter."""
        
        connect_str = self.driver + "://" + str(self.username) + \
                                    ":"   + str(self.password) + \
                                    "@" + str(self.host) + \
                                    ":" + str(self.port) + \
                                    "/" + str(self.database) + \
                                    "?charset=" + self.charset
                                    
        print "**[INFO]** Connecting to database: " + connect_str
        print "**[INFO]** Sqlalchemy version: " + sqlalchemy.__version__
        self._engine = sqlalchemy.create_engine(connect_str, echo = False)
        self._conn = self._engine.connect()
                
    def reconnect(self):
        """
        re-connect db connection
        """
        if self._conn is None:
            if self._engine is None:
                self.connect()
            else:
                self._conn = self._engine.connect()
                    
    def close(self):
        self._conn.close()
        self._engine.dispose()
        print "**[INFO]** DB connection closed..."
               
    def execute(self, sql_clause, close_conn = False):
        '''
        execute sql sentence
        @var sql_clause: sql sentence
        @var close_conn: if close_conn is true, it will be close the database connection
        @return: return the list of sql
        '''
        sql_clause = sql_clause.rstrip(';')
       
        if self._conn is None:
            self.reconnect()
            print "**[INFO]** DB connection is re-connected..."
        try:
            result = self._engine.execute(sql_clause)
        except Exception, e:
            raise
        finally:
            if close_conn:
                self.close()
            else:
                pass
        return result
    
    def get_row(self, sql_clause, close_conn = False):
        
        """Get ONE row which is instance of sqlalchemy.engine.base.RowProxy 
        @var sql_clause: string, sql
        @var close_conn: boolean, if close_conn is True, it will close the connection when data is returned. 
                                  if close_conn is default: False, we should call close function in the end. or __del__ delete them.
        @return: list, one row
        @result: (data, data, data,)
        """
        result = self.execute(sql_clause, close_conn).fetchone()
        return result
    

    def get_rows(self, sql_clause, close_conn = False):
        """
        Get all the rows which are instance of sqlalchemy.engine.base.RowProxy
        @var sql_clause: string, sql
        @var close_conn: boolean, if close_conn is True, it will close the connection when data is returned. 
                                  if close_conn is default: False, we should call close function in the end. or __del__ delete them.
        @return: a list of containing rows
        """
        result = self.execute(sql_clause, close_conn).fetchall()
        return result
    
    
    def get_count(self, sql_clause, close_conn = False):

        rows = self.get_rows(sql_clause, close_conn)
        return len(rows)
        
    @classmethod
    def get_common_db_config_full_path(cls):
        #get current python file path, not current execute file path
        current_path = dirname(abspath(__file__))
        return join(current_path, '..', Settings.COMMON_DB_CONF_PATH)
        
        