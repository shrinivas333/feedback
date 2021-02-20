
# from django.urls import path,include
# from .views import FeedbackView,QuestionsViewSet,AnswersViewSet,FeedbackResponse,ChoiceViewset,AnswersView,FormsViweSet
# from rest_framework import routers
# from.models import Questions,Choices

# router=routers.DefaultRouter()
# router.register('question',QuestionsViewSet, basename="question")
# router.register('answers',AnswersViewSet,basename='answers')
# router.register('answer',AnswersView,basename='answer')
# router.register('choices',ChoiceViewset,basename='choices'),
# router.register('forms',FormsViweSet,basename='forms')

# urlpatterns = [
#     path('api/',include(router.urls)),
#     path('', FeedbackView,name='FeedbackView'),
#     path('response/', FeedbackResponse,name='Response'),
#     path('api-auth/', include('rest_framework.urls')),
# ]