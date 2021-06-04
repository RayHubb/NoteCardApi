from rest_framework import serializers
from .models import NoteCard
from .models import Collection
class NoteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCard
        fields = ['id', 'question', 'answer', 'collection']

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']