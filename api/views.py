from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# Function Based views
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def index(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        message = 'This URL is working'
        return Response(data=message, )
    elif request.method == 'POST':
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        print(Response(data='Invalid request'))


# Class Based Views

class Message(APIView):
    def get(self):
        return Response(data='This is a class based view')
