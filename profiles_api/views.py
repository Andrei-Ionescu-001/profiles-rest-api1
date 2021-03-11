from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    """test"""
    serializer_class=serializers.HelloSerializer


    def get(self, request, format=None):
        """returns a list of apiviews features"""
        an_apiview=[
            'uses HTTP methods a function',
            'is similar to a tradional django view',
            'gives you the most control over the app logic',
            'mapped manually to urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with out name"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})
    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
