from rest_framework import serializers
from .models import Questions,Choices,Answers

class ChoiceSrializer(serializers.ModelSerializer):

    class Meta:
        model=Choices
        fields=('id','choice_name')

class QusetionSerializer(serializers.ModelSerializer):
    choices=ChoiceSrializer(many=True)

    class Meta:
        model=Questions
        fields=('question_id','choices','qusetion_name','question_type','date')

class AnswerSerializer(serializers.ModelSerializer):

    question=QusetionSerializer(many=False)

    class Meta:
        model=Answers
        fields=('answer_id','description','question','user',)