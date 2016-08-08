from __future__ import unicode_literals
from django.db import models

'''
 author: Chen Jinyu
 email: jinyu2010.chen@gmail.com
 date: 2016-05-04
 '''
 
 
class ProLiant_DL_Server(models.Model):
    
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    title = models.CharField(max_length = 140)
    img = models.CharField(max_length = 140)
    description =  models.TextField()
    
    def __str__(self):
        return self.title
    
class ProLiant_DL300_Servers(models.Model):
    
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    title = models.CharField(max_length = 140)
    img = models.CharField(max_length = 140)
    description =  models.TextField()
    
    def __str__(self):
        return self.title
    
    
class ProLian_DL_Customize_Factory(models.Model):
    
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    title = models.CharField(max_length = 140)
    price = models.CharField(max_length = 140)
    description =  models.TextField()
    
    def __str__(self):
        return self.title
    
    
class ProLian_DL_Customize_Field(models.Model):
    
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    title = models.CharField(max_length = 140)
    price = models.CharField(max_length = 140)
    description =  models.TextField()
    
    def __str__(self):
        return self.title
    
class Memory_DB(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    type = models.CharField(max_length = 10)
    part_num = models.CharField(max_length = 50)
    description = models.CharField(max_length = 140)
    price = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.part_num
    
class Storage_DB(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    type = models.CharField(max_length = 10)
    part_num = models.CharField(max_length = 50)
    description = models.CharField(max_length = 140)
    price = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.part_num
    
class Processor_DB(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID')
    type = models.CharField(max_length = 10)
    part_num = models.CharField(max_length = 50)
    description = models.CharField(max_length = 140)
    price = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.part_num
    
    