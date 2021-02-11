from django.db import models

# Create your models here.

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
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qusetion_name
    
    def saveQusetions(self,data):
        print(data)
        question=Questions()
        question.qusetion_name=data['qusetion_name']
        question.question_type=data['question_type']
        question.save()
        choices_list=Choices.addchoice(data['choices'])
        for choice in choices_list:
            question.choices.add(choice)

        return question

