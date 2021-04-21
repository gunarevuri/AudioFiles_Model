from .models import Podcast,Song,Audiobook

from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['Name','']