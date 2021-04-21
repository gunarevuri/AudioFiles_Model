from django.shortcuts import render

from rest_framework import status
from rest_framework.parsers import JSONParser


from .models import Podcast,Song,Audiobook
from .serializers import *


from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


@api_view(["GET"])
def Get_Audios(request,audioFileType):
    if audioFileType  == 'Song':
        pass
    elif audioFileType == ''
    try:
        songs  = Song.objects.all()
        serialized_songs = 
@api_view(["GET","POST","DELETE"])
