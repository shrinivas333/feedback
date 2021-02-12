from rest_framework import serializers
from .models import Questions,Choices

class ChoiceSrializer(serializers.ModelSerializer):

    class Meta:
        model=Choices
        fields=('id','choice_name')

class QusetionSerializer(serializers.ModelSerializer):
    choices=ChoiceSrializer(many=True)

    class Meta:
        model=Questions
        fields=('question_id','choices','qusetion_name','question_type','date')

 