from django.shortcuts import render

from rest_framework import status
from rest_framework.parsers import JSONParser


from .models import Podcast,Song,Audiobook
from .serializers import SongSerializer,PodcastSerializer,AudiobookSerializer


from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import os
import logging

logger = logging.getLogger(__name__)

log_path = os.getcwd()+'application.log'

try:
    os.path.join(log_path)
except Exception as e:
    print(e)
    os.mkdir(log_path)

f_handler = logging.FileHandler(log_path)
f_handler.setLevel(logging.DEBUG)


f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)


logger.addHandler(f_handler)



@api_view(["GET"])
def Get_Audios(request,audioFileType=None,audioFileID=None):
    if audioFileType  == 'Song':
        try:
            if audioFileID:
                song = Song.objects.filter(ID  = audioFileID)

            else:
                songs  = Song.objects.all()
                serializer = SongSerializer(songs,many=True)
                return Response(data=serializer.data,status=200)
                
        except Exception as e:
            print(e)
            logger.error(e,exc_info=True)

    elif audioFileType == 'Podcast':
        pass
    else:
        pass


@api_view(["POST"])
def Del_Audio(request,audioFileType,audioFileID):
    pass