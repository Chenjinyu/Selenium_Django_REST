from rest_framework import serializers
from storage.models import Storage, LOCATIONS


class StorageSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Storage
        fields = ('id', 'title', 'description', 'avaliable', 'location')
        
    