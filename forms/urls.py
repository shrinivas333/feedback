
from django.urls import path,include
from .views import FeedbackView,QuestionsViewSet
from rest_framework import routers
from.models import Questions,Choices

router=routers.DefaultRouter()
router.register('question',QuestionsViewSet, basename="question")


urlpatterns = [
    path('api/',include(router.urls)),
    path('', FeedbackView),
]