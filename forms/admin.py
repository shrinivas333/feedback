from django.contrib import admin
from .models import Questions,Choices,Answers
# Register your models here.

admin.site.register(Questions)
admin.site.register(Choices)
admin.site.register(Answers)