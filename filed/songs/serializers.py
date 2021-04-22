from .models import Podcast,Song,Audiobook

from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['ID','Name','Song_Duration','Upload_Time']

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['ID','Podcast_Name','Podcast_Duration','Upload_Time','Host','Participants']

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ['ID','Title','Author','Narrator','Audiobook_Duration','Upload_Time']

    