#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This project just is a demo for intel.
Email: jinyu2010.chen@gmail.com
"""

import os
import unittest

from Libs import HTMLTestRunner
# from Libs import XMLTestRunner
from Libs import ParserConfigFile
from Libs import FileAndConsoleLogConfig
from Libs import CommonFuns

from Testcases import *


if __name__ == '__main__': 
    
    proj_root = CommonFuns.get_project_root()
    read_config = ParserConfigFile(os.path.join(proj_root,'gui_testsuites_demo.cfg'))
    is_email = read_config.get_item_value('EMAIL','send_email')
    
    # create a log object which print log info into log file and console at the same time
    logging = FileAndConsoleLogConfig(level = 'INFO')
    logging.info("**[INFO]** Demo GUI Test --->>>")
    try:
        all_test_suites = unittest.TestSuite([unittest.makeSuite(SelectProductFunsTestCase, 'test'),
                                                       unittest.makeSuite(SolutionsMenuDropdownListTestCase, 'test'),
                                                       unittest.makeSuite(ServicesMenuDropdownListTestCase, 'test'),
                                                                        ])
        
#         # generate test report with xml file.
#         export_reprot_pathname = os.getcwd() + os.sep + "Reporters" + os.sep + "demo_select_product_test_report.xml"
#         file_open_handler = file(export_reprot_pathname,'wb')
#         runner = XMLTestRunner(stream = file_open_handler)
#     
#         test_result = runner.run(all_test_suites).wasSuccessful()

        # generate test report with html file.
        export_reprot_pathname = os.getcwd() + os.sep + "Reporters" + os.sep + "demo_select_product_test_report.html"
        file_open_handler = file(export_reprot_pathname, 'wb')
        runner = HTMLTestRunner(
                    stream = file_open_handler,
                    title='My Demo Unit Test',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
         
        # run the test
        test_result = runner.run(all_test_suites).wasSuccessful()
  
    except Exception, e:
        logging.error(e)
        test_result = False
        print e
    finally:
        file_open_handler.close()

    result_str = lambda result: 'Successful' if result else 'Failed'
    
    if is_email == 'True':
        from Libs import Gmail
        subject = 'Functional Testing %s  -- [%s]' % (result_str(test_result), CommonFuns.get_current_timestamp())
        content = '''
Hi, Team

This is a demo test report, please see the attachment.

Best,
Automation Team
'''
        try:
            email_handler = Gmail()
            email_handler.send_email_with_attachs(subject, content, os.path.join(proj_root, 'Reporters/demo_select_product_test_report.html'))
            logging.info('Send email successfully to team.')
        except Exception, e:
            logging.error('Send email error: %s' % e)
        
    logging.info("----------------------------------")
    logging.info("| Demo web testing %s. |" % result_str(test_result))
    logging.info("----------------------------------")
    logging.info("**[INFO]** <<<--- Demo GUI Test")

