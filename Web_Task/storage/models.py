from __future__ import unicode_literals

from django.db import models

LOCATIONS = [('USA', 'The United States'), ('China', 'PR. China')]


class Storage(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = False)
    description = models.TextField()
    avaliable = models.BooleanField(default = True)
    location = models.CharField(choices = LOCATIONS, default = 'The United States', max_length = 50)
    
    class Meta:
        ordering = ('created', )