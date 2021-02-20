# from rest_framework import serializers
# from .models import Questions,Choices,Answers,Users,Forms

# class ChoiceSrializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Choices
#         fields=('id','choice_name')

# class UsersSrializer(serializers.ModelSerializer):

#     class Meta:
#         model=Users
#         fields=('id','name','phone')

# class QusetionSerializer(serializers.ModelSerializer):
#     choices=ChoiceSrializer(many=True)

#     class Meta:
#         model=Questions
#         fields=('question_id','choices','qusetion_name','question_type','required','date')

# class AnswerSerializer(serializers.ModelSerializer):

#     question=QusetionSerializer(many=False)

#     class Meta:
#         model=Answers
#         fields=('answer_id','description','question','email','date')

# class FormSerializer(serializers.ModelSerializer):
#     questions=QusetionSerializer(many=True)
#     answers=AnswerSerializer(many=True)
#     url=serializers.SerializerMethodField()
#     class Meta:
#         model=Forms
#         fields=('id','title','description','template','url','questions','answers','date')

#     def get_url(self,instance):
#         print(instance)
#         return 'http://127.0.0.1:8000/feedback/?template=template2&&form='+str(instance.id)
    