from django.shortcuts import render
from .models import Questions,Choices,Answers
from .serializer import ChoiceSrializer,QusetionSerializer,AnswerSerializer
from rest_framework import viewsets, mixins,serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import BasePagination
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import action


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20




@csrf_exempt
def FeedbackView(request):
    print(request.POST)
   
    if request.method=='GET':
        questions=Questions.objects.all()
        return render(request,'forms/feedback2.html',{'questions':questions})
    
    elif  request.method=='POST':
        answers=json.loads(request.body)
        email=answers['email']
        print(email)
        answers=answers['answers']
        try:
            answers=Answers.addAnswers(answers,email)
        except:
            answers=None
        if answers is not None:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
def FeedbackResponse(request):
    return render(request,'forms/inputText.html')



class AnswersView(viewsets.ModelViewSet):
    queryset=Answers.objects.all()
    serializer_class=AnswerSerializer
    pagination_class=StandardResultsSetPagination
    filter_fields = ('question__question_id',)
   
    
        
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset=Questions.objects.all()
    serializer_class= QusetionSerializer

    def create(self,request):
        print(request.data)
        question=Questions.saveQusetions(self,request.data)
        return HttpResponse(json.dumps(question))

class ChoiceViewset(viewsets.ModelViewSet):
    queryset=Choices.objects.all()
    serializer_class=ChoiceSrializer

class AnswersViewSet(viewsets.ModelViewSet):
    queryset=Answers.objects.all()
    serializer_class=AnswerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class=StandardResultsSetPagination
    filter_fields = ('email','question__question_id')

    @action(detail=True, methods=['Get'])
    def get_ans_info(self,request,pk=None):
        print(pk)
        question=Questions.objects.get(pk=pk)
        print(question.choices.all())
        choices=question.choices.all()
        answers=Answers.objects.all().filter(question__question_id=pk)
        answers_count=Answers.objects.all().filter(question__question_id=pk).count()
        print(answers_count)
        choice_list=[]
        for choice in choices:
            print(choice.choice_name)
            count=answers.aggregate(Avg(description=choice))
            print(count)
            choicedict={'choice':choice.choice_name,'count':count}
            choice_list.append(choicedict)
        print(choice_list)
        outputDict={}
        
        outputDict['count']=answers_count
        outputDict['result']=choice_list
       
        return HttpResponse(json.dumps(outputDict))
