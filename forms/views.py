from django.shortcuts import render
from .models import Questions,Choices,Answers
from .serializer import ChoiceSrializer,QusetionSerializer,AnswerSerializer
from rest_framework import viewsets, mixins,serializers
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def FeedbackView(request):
    print(request.POST)

    answers=json.loads(request.body)
    answers=answers['answers']
    for i in answers:
        print(i['id']+ " : "+ i['answer'])

    if request.method=='POST':
        print(json.dumps(request.POST))
        Answers.addAnswers(request.POST)
    if request.method=='GET':
        questions=Questions.objects.all()
        return render(request,'forms/feedbackForm.html',{'questions':questions})
        # return render(request,'forms/demo.html')


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset=Questions.objects.all()
    serializer_class= QusetionSerializer

    def create(self,request):
        print(request.data)
        question=Questions.saveQusetions(self,request.data)
        return question

class AnswersViewSet(viewsets.ModelViewSet):
    queryset=Answers.objects.all()
    serializer_class=AnswerSerializer