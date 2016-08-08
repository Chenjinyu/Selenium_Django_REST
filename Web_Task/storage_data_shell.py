from storage.models import Storage
from storage.serializers import StorageSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

storage = Storage(title = 'HP StoreEver LTO-5 Ultrium SB3000c Tape Blade', description = "The \
HP Ultrium Tape Blades are ideal for HP BladeSystem c-Class customers who need an integrated data \
protection solution. \nThese half-height tape blades provides direct attach data protection for the adjacent \
server and network backup protection for all data residing within the enclosure. \nHP Ultrium Tape Blades \
offer a complete data protection, \ndisaster recovery and archiving solution for BladeSystem c-Class customers.")
storage.save()

storage = Storage(title = 'Business Class Libraries', description = 'Up to 16 tape drives and 240 slots with a choice of tape technologies.\n\
Investment protection with both capacity and performance upgrades for environments with unpredictable data growth')
storage.save()

serializer = StorageSerializer(storage)
serializer.data