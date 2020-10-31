
from django.contrib.auth.models import User
from rest_framework import serializers


from api.models import Dog
from api.models import Breed


class DogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']
    
    
    def create(self, validated_data):
        """
        Create and return a new `Dog` instance, given the validated data.
        """
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Dog` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance

class BreedSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds'] 

    def create(self, validated_data):
        """
        Create and return a new `Breed` instance, given the validated data.
        """
        return Dog.objects.create()
    def update(self, instance, validated_data):
        """
        Update and return an existing `Breed` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance

 