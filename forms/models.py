from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=10, default=None,)

class Choices(models.Model):
    id=models.AutoField(primary_key=True)
    choice_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.choice_name

        
    @staticmethod
    def addchoice(data):
        print(data)
        choice_list=[]
        for i in data:
            try:
                choice=Choices.objects.get(pk=i['id'])
            except:
                choice=None
            if choice is None:
                choice=Choices(choice_name=i['choice_name'])
                choice.save()
            choice_list.append(choice)
        return choice_list
        

class Questions(models.Model):
    YESORNO=0;
    CHOICESTYPE=1;
    RATING=2;
    INPUTTYPE=3;
    QUSETION_CHOICE = ((YESORNO, "yesorno"), (CHOICESTYPE, "choiceType"),(RATING,'rating'),(INPUTTYPE,'inputType'))

    question_id=models.AutoField(primary_key=True)
    choices=models.ManyToManyField(Choices,related_name='question',blank=True,null=True)
    qusetion_name=models.CharField(max_length=250)
    question_type=models.SmallIntegerField(choices=QUSETION_CHOICE,default=INPUTTYPE)
    required=models.BooleanField(default=False)

    date=models.DateTimeField(auto_now_add=True)

    
    
    def saveQusetions(self,data):
        print(data)
        question_list=[]
        for i in data:
            question=Questions()
            question.qusetion_name=i['qusetion_name']
            question.question_type=i['question_type']
            question.save()
            choices_list=Choices.addchoice(i['choices'])
            for choice in choices_list:
                question.choices.add(choice)
            question_list.append(question)
        return question_list

    def updateQuestion(self,data):
        print(data)
        question=Questions()
        question.qusetion_name=data['qusetion_name']
        question.question_type=data['question_type']
        question.save()
        choices_list=Choices.addchoice(data['choices'])
        for choice in choices_list:
            question.choices.add(choice)
        return question

class Answers(models.Model):
    answer_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=300,null=True)
    question=models.ForeignKey(Questions,default=None,null=True, on_delete=models.CASCADE)
    email=models.EmailField(default=None)
    date=models.DateTimeField(auto_now_add=True)

    
    @staticmethod
    def addAnswers(data,email):
        answer_list=[]
        for i in data:
            print(email)
            answer=Answers()
            answer.email=email
            answer.description=i['answer']
            answer.question=Questions.objects.get(pk=i['id'])
            answer.save()
            answer_list.append(answer)
        return answer_list

            
class Forms(models.Model):
    TEMPLATE1=1;
    TEMPLATE2=2;
    TEMPLATE_CHOICE = ((TEMPLATE1, "template1"), (TEMPLATE2, "template2"))

    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    questions=models.ManyToManyField(Questions,default=None)
    template=models.SmallIntegerField(choices=TEMPLATE_CHOICE,default=TEMPLATE1)
    answers=models.ManyToManyField(Answers,default=None,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    @staticmethod
    def updateanswer(data,email,id):
        print(id)
        form=Forms.objects.get(id=id)
        answers=Answers.addAnswers(data,email)
        for answer in answers:
            form.answers.add(answer)
        
        return form

    @staticmethod
    def createForms(self,data):
        form=Forms()
        form.title=data['title'],
        form.description=data['description']
        form.template=data['template']
        form.save()
        questions=Questions.saveQusetions(self,data['questions'])
        for ques in questions:
            form.questions.add(ques)
        
        return form

    @staticmethod
    def updateQuestion(self,id,data):
        form=Forms.objects.get(id=id)
        question=Questions.updateQuestion(self,data['questions'])
        form.save()
        form.questions.add(question)
        
        return form