from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """test"""

    def get(self, request, format=None):
        """returns a list of apiviews features"""
        an_apiview=[
            'uses HTTP methods a function',
            'is similar to a tradional django view',
            'gives you the most control over the app logic',
            'mapped manually to urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
