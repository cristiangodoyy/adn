from rest_framework import serializers
from .models import Dna


class DnaSerializer(serializers.Serializer):
    dna = serializers.ListField(required=True)

    def create(self, validated_data):
        """
        Create and return a new Dna instance, given the validated data.
        """
        return Dna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Dna instance, given the validated 
        data.
        """
        instance.dna = validated_data.get('dna', instance.dna)
        instance.save()
        return instance
