from django.contrib import admin
from HP_SimplifiedConfig.models import ProLiant_DL_Server,ProLiant_DL300_Servers, \
ProLian_DL_Customize_Field, ProLian_DL_Customize_Factory, Memory_DB, Storage_DB, Processor_DB

admin.site.register(ProLiant_DL_Server) 
admin.site.register(ProLiant_DL300_Servers) 
admin.site.register(ProLian_DL_Customize_Field) 
admin.site.register(ProLian_DL_Customize_Factory) 
admin.site.register(Memory_DB) 
admin.site.register(Storage_DB) 
admin.site.register(Processor_DB) 