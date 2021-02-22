from django.shortcuts import render
from .models import Questions,Choices,Answers,Forms
from .serializer import ChoiceSrializer,QusetionSerializer,AnswerSerializer,FormSerializer
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
    formval = request.GET.get("form",'')
    templateval = request.GET.get('template','')

    if request.method=='GET':
        print(formval)
        if formval is not None:
            form=Forms.objects.get(id=formval)
            questions=form.questions.all()
            print(questions)
            if 'template1' in templateval:
                return render(request,'forms/feedback2.html',{'questions':questions})
            elif 'template2' in templateval:
                return render(request,'forms/feedbackForm.html',{'questions':questions})
        
    
    elif  request.method=='POST':
        answers=json.loads(request.body)
        email=answers['email']
        id=answers['id']
        print(id)
        answers=answers['answers']
        try:
            answers=Forms.updateanswer(answers,email,id)
            print(answers)
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
    filter_fields = ('email','question__question_id',)

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
            count=answers.filter(description=choice).count()
            print(count)
            choicedict={'choice':choice.choice_name,'count':count}
            choice_list.append(choicedict)
        print(choice_list)
        outputDict={}
        
        outputDict['count']=answers_count
        outputDict['result']=choice_list
       
        return HttpResponse(json.dumps(outputDict))


class FormsViweSet(viewsets.ModelViewSet):
    queryset=Forms.objects.all()
    serializer_class=FormSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class=StandardResultsSetPagination
    filter_fields = ('id','questions__question_id',)

    

    def create(self,request):
        print(request.data)
        form=Forms.createForms(self,request.data)
        outputDict={}
        url='http://127.0.0.1:8000/feedback/?template=template'+str(form.template)+'&&form='+str(form.id)
        print(url)
        outputDict['url']=url
        return HttpResponse(json.dumps(outputDict))
    
    @action(detail=True, methods=['patch'], name="updated qustions")
    def questions(self, request, pk=None):
        print(request.data)
        form= Forms.updateQuestion(self,pk,request.data)
        outputDict={}
        if form is not None:
            outputDict['message']="updated Sucessfully"
        else:
            outputDict['message']="unsucessfull"
        return HttpResponse(json.dumps(outputDict))