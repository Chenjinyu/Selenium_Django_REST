"Selenium_Django_REST"

Web_Task is a django project, it uses a easy way to simulate some pages of https://sce-public.houston.hp.com/SimplifiedConfig/Welcome. and in it has a easy demo of how to develop REST. 
Seleniun_Demo_Proj uses selenium python library and to test the django website. it has some very useful common libraries which developed by myself.
1. Database library, it a esay way to config and use them.
2. Config, it has EmailConfig.py which shows us how to send email via Gmail; LogConfig.py which shows us a easy way to record our errors, warnings, infos, and log file will be deleted by automatically; ParserConfigFile.py is used for parser cfg file. 


how to install Django(below steps run on windows):

1. Download Python 3.5 from official website. it will help us install like pip, easy_install, etc.

2. pip install virtualenv to install virtualenv tool which is very useful for multi django projects on your local develpment computer.

3. go to a folder whatever you want. and use command 'virtualenv djang_env' to create a python virtual environment. we will see it will use python 3.5 which you installed on your comptuer to install the new virtual enviroment. that means if you want to install a virtualenv which depends on python 2.7, you need to install python 2.7, and install the virtualenv on your python2.7/lib/site-pacakges, and at the same time, the command of virtualenv cames from python2.7. you must change the path system variables.

4. go to the virtualenv folder, you will see the several folder here. input the command: 'Scripts\activate', it will activate the virtualenv.

5. use command: 'pip install django', it will install the newest version of django for you. if you want to install like django 1.9, use 'pip install django==1.9'

6. pip install django-bootstrap3

7. pip install djangorestframework, requests, pygments, rest_framework

8. django-admin createproject xxx

9. copy the survery_form app to your django project.

10. add the survery_form to your settings/INSTALLED_APPS.

11. go to the django project folder, and command 'python manage.py makemigrations'.

12. python manage.py migrate.

13. python manage.py runserver.

14. Done

How to Install selenium(below steps run on windows):
1. pip install selenium
2. other associate libraries, sorry i forget its a long ago.


python manage.py runserver, make sure the website can be visited. go to Seleniun_Demo_Proj, and run gui_testsuites_demo.py.
it will generate log file and demo_select_product_test_report.html or demo_select_product_test_report.xml.


keywords: Django, Selenium DjangoRestframework, EmailConfig, Database, ParserConfigFile, etc.

hope useful for you. good luck guys.
