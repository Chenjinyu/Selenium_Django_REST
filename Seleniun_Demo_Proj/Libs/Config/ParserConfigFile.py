"""
Use this class to read and write config
Author: jinyu2010.chen@gmail.com
Date: 05/25/2016

example:
[DEFAULT]
option_d_1 = value_d_1
option_d_2 = value_d_2

[SECTION_NAME]
option_1 = value_1
option_2 = value_2
"""

import os
import sys
import codecs
from ConfigParser import SafeConfigParser

__version__ = '0.0.1'


class ParserConfigFile(SafeConfigParser):
    
    
    def __init__(self, config_filename_list, raise_error = False, is_unicode = False):
        """
        @var config_filename: config full path
        @var raise_error: if raise_error is True, it will raise error when error is happened
        @var is_unicode: if is_unicode is True, could read unicode content 
        """
        
        self.config_parser = SafeConfigParser()
        
        self.config_filename_list = []
        if not isinstance(config_filename_list, (list, tuple)):
            self.config_filename_list.append(config_filename_list)
        else:
            self.config_filename_list = config_filename_list
    
        for filename in self.config_filename_list:
            if not os.path.exists(filename):
                raise Exception('Config File[%s] could not be find...' % filename)
    
        self.is_unicode    = is_unicode
        self.raise_error = raise_error
        
        if len(self.config_filename_list):
            try:
                if self.is_unicode is True:
                    # Open the file with the correct encoding
                    with codecs.open(self.config_filename_list, 'r', encoding='utf-8') as config_file:
                        self.config_parser.readfp(config_file)
                else:
                    self.config_parser.read(self.config_filename_list)
            except Exception, e:
                print "**[ERROR]** read config file error, %s" %e
                if self.raise_error:
                    raise
        else:
            print "**[ERROR]** config filename is error"
            if self.raise_error:
                raise Exception("**[ERROR]** config filename is error")
        
    def print_config_info(self):
        
        self.config_parser.write(sys.stdout)
        
        
    def get_sections(self):
        """
        get all of sections in cfg file, excluding [DEFAULT]
        @return: return a list like ['SECTION_NAME']
        """
        return self.config_parser.sections()
    
    
    def get_options(self, section_name):
        """
        get a list via the section name. 
        eg. get_options('SECTION_NAME').
        return ['option_1', 'option_2']
        @return: return a list with the section name.
        """
        
        return self.config_parser.options(section_name)


    def get_default(self):
        """
        get the default section options and values
        return {'option_d_1': 'value_d_1', 'option_d_2': 'value_d_2'}
        @return: it will return the dict with options and values in the DEFAULT section.
        """
        return self.config_parser.defaults()
    
    
    def get_items(self, section_name):
        """
        get a list of tuples with (name, value) for each option in the section. 
        if the section_name is 'DEFAULT', it will get the same data with get_default
        @var: section name
        @return: a list
        """
        return self.config_parser.items(section_name)


    def get(self, section_name, option_name, raw = False, vars = None):
        """
        Some script also use get to get config info
        """
        return self.config_parser.get(section_name, option_name, raw, vars)


    def get_item_value(self, section_name, option_name):
        """
        get option's value.
        """
        return self.config_parser.get(section_name, option_name)


    def get_items_list(self, section_name):
        """
        return options with list
        """
        option_list = self.get_options(section_name)
        item_list = []
        for option in option_list:
            item_list.append(self.get_item_value(section_name, option))
        return item_list
    
    
    def get_items_dict(self, section_name):
        """
        return options with dictionary.
        """
        option_list = self.get_options(section_name)
        item_dict = {}
        for option in option_list:
            item_dict[option] = self.get_item_value(section_name, option)
        return item_dict
       
       
    def update_current_config_file(self, section, item, value):
        """
        update one item value in one section.
        """
        if section not in self.get_sections():
            print "**[ERROR]** Can not find section name %s." % section
        else:
            try:
                self.config_parser.set(section, item, value)
            except Exception, e:
                print "**[ERROR]** update_current_config_file occurs: %s" % e
                if self.raise_error:
                    raise
            self.__write_config()
    
    
    def set(self, section, option, value):
        """
        re-write set function, cause some script also use config.set.
        """
        self.update_current_config_file(section, option, value)
        
        
    def save_config_file(self, config_file = None):
        """
        it will read&write config info from original file to new config one.
        """
        if config_file is None:
            raise AssertionError('config file not allow to be empty.')
        
        self.__write_config(config_file)
        
        
    def add_section(self, section_name):
        """
        add section to config file
        """
        try:
            if section_name not in self.get_sections():
                self.config_parser.add_section(section_name)
                self.__write_config()
            else:
                print "**[INFO]** section name (%s) have existed in config file." % section_name
        except Exception, e:
            print "**[ERROR]** Error occour in add_section: %s" %e
            if self.raise_error:
                raise
        
        
    def add_options(self, section_name, options_dict = None):   
        """
        @section_name: if section have not existed, it will be created
        @options_dict must be dict like:  {'option_name_1': 'option_value_1', 'option_name_2': 'option_value_2' }
        add options to section.
        """
        if section_name not in self.get_sections():
                self.config_parser.add_section(section_name)
        else:
                print "**[INFO]** section name (%s) have existed in config file." % section_name
                
        if options_dict is not None:
            for item, value in options_dict.iteritems():
                self.config_parser.set(section_name, item, value)
            self.__write_config()
        
        
    def get_special_item_value(self, section_name, option_name):
        """
        """
        return self.get_item_value(section_name, option_name).encode('utf-8')
    
    
    def get_item_value_via_type(self, section_name, option_name, value_type = ''):
        """
        get item value via type
        """
        value_type = value_type.lower()
        if value_type == 'int':
            return self.config_parser.getint(section_name, option_name)
        elif value_type == 'float':
            return self.config_parser.getfloat(section_name, option_name)
        elif value_type == 'boolean':
            return self.config_parser.getboolean(section_name, option_name)
        else: 
            return self.config_parser.get(section_name, option_name)


    def __write_config(self, config_filename = None):
        """
        @var config_filename: default is None. 
        when config_file is None, it will save into the first config file which config in inital function.
        if config is not None, it will create config file when this file have not existed. and save into new config file.
        this is a private fuction.
        """
        if config_filename is None:
            config_filename = self.config_filename_list[0] 
            
        try:
            file_open_handler = open(config_filename, 'w')
            self.config_parser.write(file_open_handler)
        except Exception, e:
            print "**[ERROR]** Error occour in write_config: %s" %e
            if self.raise_error:
                raise
        print "**[INFO]** write config have finished..."
        file_open_handler.close()
        

    