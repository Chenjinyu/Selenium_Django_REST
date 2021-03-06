from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from storage.models import Storage
from storage.serializers import StorageSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
        
@csrf_exempt
def storage_list(request):
    """
    List all storages, or create a new storage.
    """
    if request.method == 'GET':
        snippets = Storage.objects.all()
        serializer = StorageSerializer(snippets, many = True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StorageSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        return JSONResponse(serializer.errors, status = 400)
    
    
@csrf_exempt
def storage_detail(request, pk):
    """
    Retrieve, update or delete a storage.
    """
    try:
        storage = Storage.objects.get(pk = pk)
    except Storage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StorageSerializer(storage)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StorageSerializer(storage, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        storage.delete()
        return HttpResponse(status=204)