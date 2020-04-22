from rest_framework import serializers
from backend.reader.models import reader # fix import


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = reader
        fields = ['id', 'user', 'doing', 'notdoing', 'url', 'habitcount']