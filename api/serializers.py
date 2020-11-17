from rest_framework import serializers
from api.models import Dog, Breed



class DogSerializer(serializers.ModelSerializer):
    #breed = serializers.RelatedField(read_only=True)
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'age', 'gender', 'color', 'favoritefood', 'favoritetoy']

class BreedSerializer(serializers.ModelSerializer):
    #breeds = serializers.RelatedField(read_only=True)
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']        