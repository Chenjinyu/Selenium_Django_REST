"""
log file will be created with current timestamp, and it will be deleted when the data up to the default: 30.
log can be displayed on console or/and recorded into log file.
Author: Jinyu 2010.chen@gmail.com
Date: 05/24/2016
"""


import logging
import time, datetime
import fnmatch
from os import makedirs, walk, stat, walk
from os.path import join, exists
# import Toolkit

from Libs import CommonFuns
from Libs import Settings


class _LogConfig(object):
    
    
    LOG_LEVEL_LIST = {'debug'   : logging.DEBUG, 
                      'info'    : logging.INFO, 
                      'warn'    : logging.WARNING, 
                      'warning' : logging.WARNING, 
                      'error'   : logging.ERROR, 
                      'critical': logging.CRITICAL }
    
    def __init__(self, level = None, days_del_log = 30):
        
        if level is None:
            level = 'notset'
        self.logger = logging.getLogger()
        self.log_level = _LogConfig.LOG_LEVEL_LIST.get(level.lower(), logging.NOTSET)
        self.logger.setLevel(self.log_level)
        self.current_running_script_name = CommonFuns.get_current_script_name()
        if days_del_log > 0: # days_del_log = -1 is doesn't delete
            self._delete_old_log_files_by_days(days_del_log)
        
    def _output_log_to_file(self, file_name = None):
        """
        output log information to log file
        @var file_name: string. if file_name is None, it will name the log file as: [script_name]_[current_date].log
        """
        
        file_path = Settings.LOG_PATH
        if file_name is None:
            file_name = self.current_running_script_name
            
        full_file_path = join(file_path, file_name)
        file_name = file_name + '_' + CommonFuns.get_current_date() + '.log'
        
        if not exists(full_file_path):
            makedirs(full_file_path)
        try:
            file_handler = logging.FileHandler(join(full_file_path, file_name))
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(self._logging_simple_formatter())
            self.logger.addHandler(file_handler)
        except Exception, e:
            print "**[ERROR]** error happen: %s" %e
            raise
        
        
    def _delete_old_log_files_by_days(self, days_del_log):
        """
        delete old log file, the default is ON
        @var: days_del_log is a number.
        """
        current_time = datetime.datetime.now()
        for root, dirs, log_files in walk(join(Settings.LOG_PATH, self.current_running_script_name)):
            for file in log_files:
                if fnmatch.fnmatch(file, self.current_running_script_name + '_*.log'):
                    file_modify_time = time.localtime(stat(join(root, file)).st_mtime)  
                    formatted_modify_time = datetime.datetime(file_modify_time[0], 
                                                              file_modify_time[1],
                                                              file_modify_time[2], 
                                                              file_modify_time[3])  
                                                      
                    dis_days = (current_time - formatted_modify_time).days
                    if dis_days >= days_del_log:
                        Toolkit.remove(join(root, file))
                        
                    
    def _output_log_to_console(self):
        """
        output log information to console
        """
        try:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(self._logging_simple_formatter())
            self.logger.addHandler(console_handler)
        except Exception, e:
            print "**[ERROR]** error happen: %s" %e
            raise
        
        
    def _logging_formatter(self):
        return logging.Formatter("%(asctime)s:[%(levelname)s][%(module)s.%(funcName)s]: %(message)s", "%Y-%m-%d %H:%M:%S")


    def _logging_simple_formatter(self):
        return logging.Formatter("%(asctime)s:[%(levelname)s]: %(message)s", "%Y-%m-%d %H:%M:%S")


    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
        
        
    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)
        
        
    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
    
    
    def exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)
        
        
    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
        
        
    def warn(self,  msg, *args, **kwargs):
        self.warning(msg, *args, **kwargs)


    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)
    
    
    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)


class FileLogConfig(_LogConfig):
    '''
    Log will be recorded into a log file.
    '''
    def __init__(self, file_name = None, level = None, days_del_log = 30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_file(file_name)
        
    
class ConsoleLogConfig(_LogConfig):
    '''
    Log will be recorded into console.
    '''
    def __init__(self, level = None, days_del_log = 30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_console()
    
class FileAndConsoleLogConfig(_LogConfig):
    '''
    Log will be recorded into lof file and console.
    '''
    def __init__(self, file_name = None, level = None, days_del_log = 30):
        _LogConfig.__init__(self, level, days_del_log)
        self._output_log_to_file(file_name)
        self._output_log_to_console()


if __name__ == "__main__":
    #test
    test = FileAndConsoleLogConfig()
    test.info('ff')