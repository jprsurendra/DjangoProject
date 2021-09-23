from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    extra_value = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'extra_value')

    def get_extra_value(self, obj):
        return {
            'id': obj.id,
            'title': obj.title,
            'text': obj.text
        }
