"""
send plain content with mutilpate attachments email. not support send html content email at present.
Author: jinyu2010.chen@gmail.com
Date: 05/30/2016
disable it after demo: https://www.google.com/settings/security/lesssecureapps

"""

import smtplib
from os.path import join, exists, isfile, basename, dirname, abspath
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header  
from string import Template

from Libs.Config import ParserConfigFile
from Libs import Settings


class EmailConfig(object):
    
    
    def __init__(self, email_server, from_addr = None, to_addr = None, port = 587):
        
        self._smtp_obj = None
        if not email_server:
            raise Exception("Email Server can not be empty.")
        try:
            self._smtp_obj = smtplib.SMTP(email_server, port)
            self._smtp_obj.ehlo()
            self._smtp_obj.starttls()
            self._smtp_obj.ehlo()
            # login with my gmail account from private account cfg file to read.
            read_config = ParserConfigFile(EmailConfig.get_common_email_config_full_path(True))
            self._smtp_obj.login(read_config.get_item_value('ACCOUNT','username'), \
                                 read_config.get_item_value('ACCOUNT','password'))
        except Exception, e:
            print "**[ERROR]** Connect to mailhost exception occurs: %s " % e
            raise 
           
        self.from_addr = from_addr
        self.to_addr = to_addr
        
        
    def send_email(self, subject, content, from_addr = None, to_addr = None):
        if not from_addr: 
            from_addr = self.from_addr
        if not to_addr: 
            to_addr = self.to_addr
        
        if not from_addr or not to_addr:
            raise Exception('Email from address or to address can not be empty!')
        try:
            msg_content = MIMEMultipart()
            msg_content.attach(MIMEText(content, 'plain','utf-8'))
            msg_content['Subject'] = Header(subject, 'utf-8')
            msg_content['From'] = from_addr
            if isinstance(to_addr, (list, tuple)):
                msg_content['To'] = "; ".join(to_addr)
            else:
                msg_content['To'] = to_addr
                
            self._smtp_obj.sendmail(from_addr, to_addr, msg_content.as_string())
            
        except Exception, e:
            print "**[ERROR]** Send email exception error: %s " %e
            raise
        self._smtp_obj.quit()
        
        print '**[INFO]** Send email successfully' 
    
    
    def send_email_with_attachs(self, subject, content, attach_path, from_addr = None, to_addr = None):
        """
        send emai with mutilpate attachments.
        @var attach_path: string or list. the path of attachment
        """
        
        if not from_addr: 
            from_addr = self.from_addr
        if not to_addr: 
            to_addr = self.to_addr
        
        attach_path_list = []
        
        def is_attach_file_exists(attach_path):
            if isfile(attach_path): return exists(attach_path)
            else: return False
            
        if attach_path is None:
            raise Exception('attach file can not be empty')
        
        if isinstance(attach_path, (list, tuple)) is False:
            attach_path_list.append(attach_path)
        else:
            attach_path_list = attach_path
            
        for path_item in attach_path_list:
            if not is_attach_file_exists(path_item):
                print "**[EEROR]** the file path(%s) is incorrect!" % path_item
                raise Exception('attach_path is not a file or doest not exists. %s' % path_item)
        
        for path_item in attach_path_list:
            try:
                msg_content = MIMEMultipart()
                msg_content.attach(MIMEText(content, 'plain','utf-8'))
                msg_content['Subject'] = Header(subject, 'utf-8')
                msg_content['From'] = from_addr
                if isinstance(to_addr, (list, tuple)):
                    msg_content['To'] = "; ".join(to_addr)
                else:
                    msg_content['To'] = to_addr
                    
                file_open_handler = open(path_item, 'rb')
                attach_handler = MIMEText(file_open_handler.read(), 'base64', 'utf-8')  
                attach_handler.add_header('Content-Disposition', 'attachment', filename = basename(path_item))
                
                msg_content.attach(attach_handler)
                
            except Exception, e:
                print "**[ERROR]** open attach file error: %s" %e
                raise
            finally:
                file_open_handler.close()
 
        try:
            self._smtp_obj.sendmail(from_addr, to_addr, msg_content.as_string())
        except Exception, e:
            print "**[ERROR]** Send email exception error: %s " %e
            raise
        self._smtp_obj.quit()
        
        print '**[INFO]** Send email with attach file successfully' 
        
    @classmethod
    def get_common_email_config_full_path(self, pwd = False):
        #get current python file path, not current execute file path
        current_path = dirname(abspath(__file__))[:-7]
        if pwd: return join(current_path, Settings.PRIVATE_EMAIL_PWD_PATH)
        return join(current_path, Settings.COMMON_EMAIL_CONF_PATH)
        
class Gmail(EmailConfig):
    """
    get default email config information to init EmailConfig
    to_addr: 
        if is None, it will get the DEFATUT section.
        if is String, it will get the string section.
        if is List, it will get to_addr in all of list section.
    """        
    def __init__(self, section_name = None):
        file_path = EmailConfig.get_common_email_config_full_path()
        read_config = ParserConfigFile(file_path)
        if section_name is None:
            email_config_list = read_config.get_default()
        else:
            # section_name supports list or tuple. ['DEV_GROUP', 'TEST']
            if isinstance(section_name, (list, tuple)):
                email_config_list = read_config.get_default()
                to_addr_list = []
                
                for section in section_name:
                    to_addr_list.append(read_config.get_item_value(section, 'to_addr')) 
                email_config_list['to_addr']  = to_addr_list
            else: 
                email_config_list = read_config.get_items_dict(section_name)
                
        EmailConfig.__init__(self, email_config_list['email_server'], 
                                   email_config_list['from_addr'], 
                                   email_config_list['to_addr'])
        
