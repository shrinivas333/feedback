from rest_framework import serializers
from .models import Questions,Choices,Answers,Users

class ChoiceSrializer(serializers.ModelSerializer):
    
    class Meta:
        model=Choices
        fields=('id','choice_name')

class UsersSrializer(serializers.ModelSerializer):

    class Meta:
        model=Users
        fields=('id','name','phone')

class QusetionSerializer(serializers.ModelSerializer):
    choices=ChoiceSrializer(many=True)

    class Meta:
        model=Questions
        fields=('question_id','choices','qusetion_name','question_type','required','date')

class AnswerSerializer(serializers.ModelSerializer):

    question=QusetionSerializer(many=False)

    class Meta:
        model=Answers
        fields=('answer_id','description','question','email','date')