from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
import tasks.serializers as serializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.core import serializers as django_serializers
from tasks.serializers import TaskSerializer
from django.shortcuts import render, redirect  
from tasks.models import Task  

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET'])
def get(request):
    print("**********")

    task=Task.objects.all()
    print("---------------")
    if task.exists():
        departments_serializer=TaskSerializer(task,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    return HttpResponse("You have zero tasks", content_type="text/plain") 

@api_view(['POST'])
def post(request):
    data=JSONParser().parse(request)
    task_serializer = serializer.TaskSerializer(data=data)
    if task_serializer.is_valid():
            task_serializer.save()
            response = JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED) 
            print(response)
            return response
    return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Fonte: https://www.bezkoder.com/django-postgresql-crud-rest-framework/

